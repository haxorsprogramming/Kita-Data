stats = graycoprops(glcms,'Contrast Correlation Energy Homogeneity');
            Contrast = stats.Contrast;
            Correlation = stats.Correlation;
            Energy = stats.Energy;
            Homogeneity = stats.Homogeneity;
            Mean = mean2(seg_img);
            Standard_Deviation = std2(seg_img);
            Entropy = entropy(seg_img);
            RMS = mean2(rms(seg_img));
            Variance = mean2(var(double(seg_img)));
            a = sum(double(seg_img(:)));
            Smoothness = 1-(1/(1+a));
            Kurtosis = kurtosis(double(seg_img(:)));
            Skewness = skewness(double(seg_img(:)));
            % Inverse Difference Movement
            m = size(seg_img,1);
            n = size(seg_img,2);
            in_diff = 0;
            for i = 1:m
                for j = 1:n
                    temp = seg_img(i,j)./(1+(i-j).^2);
                    in_diff = in_diff+temp;
                end
            end
            IDM = double(in_diff);
%----------------------save extracted features in an array--------------------------------------------------    
            feat_disease = [Contrast,Correlation,Energy,Homogeneity, Mean, Standard_Deviation, Entropy, RMS, Variance, Smoothness, Kurtosis, Skewness, IDM];
           disp(feat_disease);
