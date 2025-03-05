import pyaudio
import wave
import threading
import tkinter as tk
from tkinter import ttk,filedialog
from datetime import datetime
import noisereduce as nr
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import os
from pydub import AudioSegment
import librosa
import soundfile as sf
import struct
import math

class AudioRecorder:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False
        self.device_index = 0
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100

    def get_input_devices(self):
        """Get all available microphone devices"""
        devices = []
        for i in range(self.p.get_device_count()):
            dev_info = self.p.get_device_info_by_index(i)
            if dev_info.get('maxInputChannels', 0) > 0:
                devices.append((i, dev_info['name'], dev_info))
        return devices

    def start_recording(self, device_index):
        """Start a new recording (automatically clear old data)"""
        self._initialize_stream(device_index)
        self.frames = []  # Reset recording data
        self.is_recording = True
        threading.Thread(target=self._record).start()

    def _initialize_stream(self, device_index):
        """Initializes the audio stream"""
        device_info = self.p.get_device_info_by_index(device_index)

        # Dynamic access to device parameters (secure)
        self.format = self.p.get_format_from_width(
            int(device_info.get('defaultSampleWidth', 2))
        )
        self.channels = int(device_info.get('maxInputChannels', 1))
        self.rate = int(device_info.get('defaultSampleRate', 44100))

        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            input_device_index=device_index,
            frames_per_buffer=1024,
            start=False
        )

    def _record(self):
        """Recording thread"""
        self.stream.start_stream()
        while self.is_recording:
            data = self.stream.read(1024)
            self.frames.append(data)
        self.stream.stop_stream()

    def pause_recording(self):
        """Pause recording"""
        self.is_recording = False

    def save_recording(self, output_dir="output"):
        """Save recording"""
        if not self.frames:
            return None  # No recording data is saved

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)


        filename = output_dir + "/origin.wav"
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
        return filename


class RecorderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ultrasonic Modulator V1.0")
        self.geometry("500x310")

        # Example Initialize recording properties
        self.recorder = AudioRecorder()
        self.last_recorded_file = None
        self.record_seconds = 0
        self.timer_id = None

        # Create interface components
        self.create_recording_section()
        self.create_modulation_section()
        self.create_status_bar()
        self.refresh_devices()

        # File saving path
        self.output_dir = None

    def create_recording_section(self):
        """Create the recording ribbon"""
        frame = ttk.LabelFrame(self, text="Recording function")
        frame.pack(pady=5, padx=10, fill=tk.X)

        # 设备选择
        ttk.Label(frame, text="Select microphone:").pack(pady=2)
        self.device_combo = ttk.Combobox(frame, width=45)
        self.device_combo.pack(pady=2)

        # 控制按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=5)

        self.btn_start = ttk.Button(btn_frame, text="Start", command=self.start)
        self.btn_stop = ttk.Button(btn_frame, text="Stop", state=tk.DISABLED, command=self.pause)
        self.btn_save = ttk.Button(btn_frame, text="Save", state=tk.DISABLED, command=self.save)

        self.btn_start.pack(side=tk.LEFT, padx=3)
        self.btn_stop.pack(side=tk.LEFT, padx=3)
        self.btn_save.pack(side=tk.LEFT, padx=3)

    def create_modulation_section(self):
        """Create the modulation function area"""
        frame = ttk.LabelFrame(self, text="Modulation function")
        frame.pack(pady=5, padx=10, fill=tk.X)

        # Modulation frequency setting
        freq_frame = ttk.Frame(frame)
        freq_frame.pack(pady=5, anchor='center')

        ttk.Label(freq_frame, text="Modulation frequency:").pack(side=tk.LEFT)
        self.mod_freq = ttk.Spinbox(freq_frame, from_=0, to=50, width=5)
        self.mod_freq.set(25)
        self.mod_freq.pack(side=tk.LEFT, padx=2)
        ttk.Label(freq_frame, text="kHz").pack(side=tk.LEFT)

        # Audio source selection
        self.audio_source = tk.StringVar(value="recorded")

        # Recording file display
        record_frame = ttk.Frame(frame)
        record_frame.pack(fill=tk.X, pady=2)
        ttk.Radiobutton(record_frame, text="Use recorded audio",
                        variable=self.audio_source, value="recorded",
                        command=self.toggle_file_input).pack(side=tk.LEFT)
        self.lbl_recorded = ttk.Label(record_frame, text="(not recorded)", foreground="gray")
        self.lbl_recorded.pack(side=tk.LEFT, padx=5)

        # File selection
        file_frame = ttk.Frame(frame)
        file_frame.pack(fill=tk.X, pady=2)
        ttk.Radiobutton(file_frame, text="Select audio file",
                        variable=self.audio_source, value="file",
                        command=self.toggle_file_input).pack(side=tk.LEFT)
        self.lbl_filename = ttk.Label(file_frame, foreground="gray")
        self.btn_browse = ttk.Button(file_frame, text="browse...",
                                     command=self.select_audio_file)


        # Start modulation button
        ttk.Button(frame, text="Start modulation", command=self.start_modulation).pack(pady=5)

    def create_status_bar(self):
        """Create status bar"""
        status_frame = ttk.Frame(self)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.time_label = ttk.Label(status_frame, text="Duration: 00:00", foreground="gray")
        self.time_label.pack(side=tk.LEFT)

        self.status = ttk.Label(status_frame, text="Ready", foreground="gray")
        self.status.pack(side=tk.RIGHT)

    def toggle_file_input(self):
        """Toggle file selection control display"""
        if self.audio_source.get() == "file":
            self.btn_browse.pack(side=tk.LEFT, padx=5)
            self.lbl_filename.pack(side=tk.LEFT)
        else:
            self.btn_browse.pack_forget()
            self.lbl_filename.pack_forget()

    def select_audio_file(self):
        """Select audio file"""
        filetypes = [("Audio file", "*.wav;*.mp3;*.ogg"), ("All files", "*.*")]
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.selected_file = filepath
            self.lbl_filename.config(text=filepath)

    def save(self):
        """Save the recording and update the display"""
        self.output_dir = "Recoder_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(self.output_dir, exist_ok=True)
        save_path = self.recorder.save_recording(self.output_dir)

        if save_path:
            self.last_recorded_file = save_path
            self.lbl_recorded.config(text=save_path)
            self.status.config(text=f"Save successfully:{save_path}", foreground="blue")
            self.btn_save.config(state=tk.DISABLED)
            self.record_seconds = 0
            self._update_time_display()

    def start_modulation(self):
        """Perform modulation operation"""
        freq = 25.0
        try:
            freq = float(self.mod_freq.get())
            if not 0 <= freq <= 50:
                raise ValueError("The frequency should be between 0 and 50kHz")
        except Exception as e:
            self.status.config(text=str(e), foreground="red")
            return

        # Gets the input file path
        if self.audio_source.get() == "recorded":
            if not self.last_recorded_file:
                self.status.config(text="Record and save the audio first", foreground="red")
                return
            input_path = self.last_recorded_file
        else:
            if not hasattr(self, 'selected_file'):
                self.status.config(text="Please select an audio file", foreground="red")
                return
            input_path = self.selected_file
            self.output_dir = "Select_" + datetime.now().strftime("%Y%m%d_%H%M%S")
            # Since the output directory was not created when the file was selected, it is created here
            os.makedirs(self.output_dir, exist_ok=True)

        # Execute modulation (Example implementation)
        self.status.config(text="Start modulattion", foreground="orange")
        # 1. Turn to wav mono
        single_file_path = convert_to_wav(input_path, self.output_dir)
        self.status.config(text="Go to wav mono", foreground="orange")
        # 2. Noise reduction
        denoise_file_path = audio_denoise(single_file_path, self.output_dir)
        self.status.config(text="Noise reduction", foreground="orange")
        # 3, bandpass filtering
        bandpass_file_path = audio_bandpass(denoise_file_path, self.output_dir)
        self.status.config(text="Band-pass filtering", foreground="orange")
        # 4. Resampling to 96k
        to96k_file_path = audio_to_96k(bandpass_file_path, self.output_dir)
        self.status.config(text="Resampling to 96k", foreground="orange")
        # 5, am modulation
        am_file_path = audio_am(to96k_file_path, self.output_dir, int(freq*1000))
        self.status.config(text=f"Successful modulation: {am_file_path}", foreground="blue")


    def refresh_devices(self):
        """Refreshing the Device list"""
        devices = self.recorder.get_input_devices()
        self.device_combo['values'] = [f"{i}: {name}" for i, name, _ in devices]
        if devices:
            self.current_device = devices[0][0]
            self.device_combo.current(0)

    def start(self):
        """Start a new recording"""
        self.record_seconds = 0  # Reset the timer
        self._update_time_display()
        device_index = int(self.device_combo.get().split(":")[0])
        self.recorder.start_recording(device_index)
        self._update_ui_state(recording=True)
        self.status.config(text="On recording...", foreground="green")
        self._start_timer()

    def _start_timer(self):
        """启动计时器"""
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.timer_id = self.after(1000, self._update_timer)

    def _update_timer(self):
        """Start timer"""
        if self.recorder.is_recording:
            self.record_seconds += 1
            self._update_time_display()
            self.timer_id = self.after(1000, self._update_timer)

    def _update_time_display(self):
        """Formatted time display"""
        mins, secs = divmod(self.record_seconds, 60)
        self.time_label.config(text=f"During: {mins:02d}:{secs:02d}")

    def pause(self):
        """Pause recording"""
        self.recorder.pause_recording()
        self._update_ui_state(recording=False)
        self.status.config(text="Paused", foreground="orange")
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None


    def _update_ui_state(self, recording):
        """Update button status"""
        self.btn_start.config(state=tk.DISABLED if recording else tk.NORMAL)
        self.btn_stop.config(state=tk.NORMAL if recording else tk.DISABLED)
        self.btn_save.config(state=tk.NORMAL if not recording else tk.DISABLED)


def convert_to_wav(origin_file_path, output_dir):
    """Convert any audio file to wav format, keeping the original sampling rate, number of channels, and bit depth"""
    try:
        # Read files (automatic recognition format)
        audio = AudioSegment.from_file(origin_file_path)

        # convert to single channel
        single_audio = audio.set_channels(1)

        # Save
        output_path = output_dir + "/1_single.wav"

        # Export to wav (keep original parameters automatically)
        single_audio.export(output_path, format="wav")
        return output_path  # Returns the path to the generated file

    except Exception as e:
        print(f"Conversion failure [{origin_file_path}]: {str(e)}")
        raise

def audio_denoise(origin_file_path, output_dir):
    # load original file
    sample_rate, data = wavfile.read(origin_file_path)
    # Executive noise suppression
    reduced_noise = nr.reduce_noise(y=data, sr=sample_rate)

    # Save
    output_path = output_dir + "/2_denoise.wav"

    # save to file
    wavfile.write(output_path, sample_rate, reduced_noise)

    return output_path

def audio_bandpass(origin_file_path, output_dir):
    # Chose bandpass parameter
    low_cut = 47.0
    high_cut = 5000.0
    order = 1

    # Load .wav file
    sample_rate, data = wavfile.read(origin_file_path)

    # bandpass filter function
    def butter_bandpass(low, high, fs, order=5):
        # Normalized to the nyquist frequency, i.e. half the sampling rate.
        nyquist = 0.5 * fs
        low = low / nyquist
        high = high / nyquist
        b, a = butter(order, [low, high], btype='band')
        return b, a

    # Set bandpass parameter
    b, a = butter_bandpass(low_cut, high_cut, sample_rate, order=order)

    # Apply the bandpass filter
    filtered_data = filtfilt(b, a, data)

    # Save
    output_path = output_dir + "/3_bandpass.wav"

    # Save the processed audio file
    wavfile.write(output_path, sample_rate, filtered_data.astype(np.int16))

    return output_path

def audio_to_96k(origin_file_path, output_dir):
    # load original file
    data, sample_rate = librosa.load(origin_file_path)

    # Set the target sampling rate
    target_sample_rate = 96000

    # Resampling audio data
    data_resampled = librosa.resample(data, orig_sr=sample_rate, target_sr=target_sample_rate)

    # Save
    output_path = output_dir + "/4_96k.wav"

    # save to file
    sf.write(output_path, data_resampled, target_sample_rate)

    return output_path

def audio_am(origin_file_path, output_dir, carry_fre=25000):
    # Import the original audio file.
    # Sample rate must be 96khz!
    sample_rate, origin_data = wavfile.read(origin_file_path)
    print("sample rate: ", sample_rate)
    if sample_rate != 96000:
        print("Sample rate must be 96khz!")
        return
    data_len = len(origin_data)
    print("data length: ", data_len)
    # Converts raw character data to integers.
    sint_data = np.frombuffer(origin_data, dtype=np.short)
    # Find the maximum volume and use it to normalize.
    data_max = max(abs(sint_data))
    print("data max: ", data_max)
    # Normalize and bigger 1.5
    int_data = sint_data * 1.0/data_max
    # # Carrier frequency of 30khz.
    # carrier = wave.open("output_carrier.wav", "w")
    # # AM-SC about f=30khz.
    # amsc = wave.open("output_amsc.wav", "w")
    # The final result of am modulation.
    output_path = output_dir + "/output_am.wav"
    am = wave.open(output_path, "w")
    # Set audio parameters.
    # for f in [am,amsc,carrier]:
    for f in [am]:
        f.setnchannels(1) # Set to single channels.
        f.setsampwidth(2) # Set to 16-bit audio.
        f.setframerate(96000) # Set to 96khz sample rate.

    # Traverse all audio data.
    for n in range(0, data_len):
        # Must: Carrier frequency - voice frequency > 20k
        # Generate a single sample of the carrier signal.
        carrier_sample = math.cos(carry_fre * (n / 96000) * math.pi * 2)
        # Generate a single sample of the AM-SC.
        signal_amsc =  int_data[n] * carrier_sample
        # Generate a single sample of the final result.
        signal_am = (int_data[n] * carrier_sample + carrier_sample) / 2

        # Store to file.
        am.writeframes(struct.pack('h', int(signal_am * data_max)))
        # amsc.writeframes(struct.pack('h', int(signal_amsc * data_max)))
        # carrier.writeframes(struct.pack('h', int(carrier_sample * data_max)))

    return output_path

if __name__ == "__main__":
    app = RecorderApp()
    app.mainloop()