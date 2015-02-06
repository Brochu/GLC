function [freq] = getFrequency (frequencyComponents, f)
    threshold = 0.85;
    freq = f(find(frequencyComponents >= (max(frequencyComponents))*threshold))