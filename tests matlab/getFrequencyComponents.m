function [components, test] = getFrequencyComponents(signal)
    Fs = 44100;
    T = 1/Fs;
    L = length(signal);
    
    nfft = 2^nextpow2(L);
    Y = fft(signal, nfft);
    NumUniquePts = ceil((nfft+1)/2);
    Y = Y(1:NumUniquePts);
    mx = abs(Y);
    mx = mx/L;
    mx = mx.^2;
    if rem(nfft, 2)
        mx(2:end) = mx(2:end)*2;
    else
        mx(2:end - 1) = mx(2:end - 1)*2;
    end
    
    f = (0:NumUniquePts-1)*Fs/nfft;
    
    %plot(f(1:1000),mx(1:1000));
    test = f;
    components = mx;