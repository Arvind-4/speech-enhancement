import numpy as np
from matplotlib import pyplot as plt


def snr(y, y_hat):
    y = np.array(y)
    y_hat = np.array(y_hat)
    noise = y - y_hat
    signal = y
    return 20 * np.log10(np.linalg.norm(signal) / np.linalg.norm(noise))


def percent_noise_removed(y, y_hat):
    y = np.array(y)
    y_hat = np.array(y_hat)
    noise = y - y_hat
    signal = y
    return np.linalg.norm(noise) / np.linalg.norm(signal)


def calculate_rms(clean_signal, noisy_signal):
    _, ax = plt.subplots(1, 1)
    ax.plot(noisy_signal, label="Noisy")
    ax.plot(clean_signal, label="Clean")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()
    plt.show()


def total_harmonic_distortion(clean_signal, noisy_signal):
    fundamental_freq_amplitude = np.abs(np.fft.fft(clean_signal)[1])
    harmonics_rms = np.sqrt(np.mean(np.square(np.fft.fft(noisy_signal)[2:])))
    thd = harmonics_rms / fundamental_freq_amplitude
    thd = thd.real
    thd_percent = thd * 100
    return thd_percent


def auto_correlation(clean_signal, noise_signal):
    autocorr = np.correlate(clean_signal, noise_signal, mode="same")
    autocorr /= np.max(autocorr)
    return autocorr


def cross_correlation(clean_signal, noise_signal):
    crosscorr = np.correlate(clean_signal, noise_signal, mode="full")
    crosscorr /= np.max(crosscorr)
    return crosscorr


def plot_correlation(clean_signal, noise_signal):
    autocorr = auto_correlation(clean_signal, noise_signal)
    crosscorr = cross_correlation(clean_signal, noise_signal)
    _, ax = plt.subplots(1, 1)
    ax.plot(autocorr, label="Auto Correlation")
    ax.plot(crosscorr, label="Cross Correlation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()
    plt.show()
