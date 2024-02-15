import librosa
import numpy as np

from model.properties import SignalAnalysis


def generate_data(input_file_path: str, output_file_path: str) -> dict:
    try:
        input_voice, _ = librosa.load(input_file_path, sr=8000)
        output_voice, _ = librosa.load(output_file_path, sr=8000)
        signal_analysis = SignalAnalysis(input_voice, output_voice)
        rms = signal_analysis.calculate_rms(is_notebook=False)
        snr = signal_analysis.sound_to_noise_ratio()
        percent = signal_analysis.percent_noise_removed()
        harmonic_distortion = signal_analysis.total_harmonic_distortion()
        correlation = signal_analysis.correlation(is_notebook=False)

        return convert_float32_to_float(
            {
                "rms": rms,
                "snr": snr,
                "percent": percent,
                "harmonic_distortion": harmonic_distortion,
                "correlation": correlation,
            }
        )

    except Exception as e:
        print(e)
        return {}


def convert_float32_to_float(data):
    if isinstance(data, dict):
        return {k: convert_float32_to_float(v) for k, v in data.items()}
    elif isinstance(data, np.float32):
        return float(data)
    else:
        return data
