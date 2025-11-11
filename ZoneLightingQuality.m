case1 = [483.3333333, 483, 738, 957.3333333; 694.5, 700, 752.3333333, 786.3333333; 897.3333333, 913.3333333, 1012.666667, 1158.666667; 859.3333333, 903.3333333, 964.6666667, 802.6666667; 452.333333333, 733, 736.3333333, 538];
case2 = [177, 476.3333333, 591.6666667, 316.3333333; 403.00, 571.6666667, 492, 417; 495.6666667, 662.6666667, 798.3333333, 526; 578, 610.6666667, 956.6666667, 558.33; 814.00, 697, 790.3333333, 463.3333333];
case3 = [328.6666667, 91.5, 161.5, 628.6666667; 466.5, 64.5, 171.6666667, 407.6666667; 493, 104.3333333, 159.3333333, 290.6666667; 375, 85.33333333, 212.6666667, 767; 48.33333333, 50.33333333, 73.33333333, 64.66666667];
case4 = [0.023333333, 0.023333333, 0.333333333, 7.266666667; 3.2, 2.6, 6.7, 22.75; 0.15, 0.113333333, 0.333333333, 7.40; 0.03, 0.04, 0.03, 0.016666667; 2.866666667, 0.03, 0.06, 0];


%Codi generat amb AI: 
%   https://www.perplexity.ai/
%   https://chatgpt.com/
%   Self-Hosted Falcon 3.3B amb Ollama i OpenWebUI
%   https://duckduckgo.com/
%   https://lumo.proton.me/
%S'han usat per fer la matriu de colors, i s'han usat per corregir les unes
%a les altres

green=[0 1 0];
red=[1 0 0];
yellow=[1 1 0];


Z = ones(size(case4));
C = nan(size(case3));

C(case4 < 300) = 1;  
C(case4 >= 300 & case4 < 400) = 2; 
C(case4 >= 400) = 3;

[X,Y] = meshgrid(1:4,1:5);

% Create figure
fig = figure('Position', [100, 100, 800, 600]);
surf(X, Y, Z, C, 'FaceAlpha', 0.7, 'FaceColor', 'interp', 'EdgeColor', 'none');
colormap([red; yellow; green]);
clim([0.5 3.5]);  % Adjust range for better interpolation
colorbar('Ticks', [1, 2, 3], 'TickLabels', {'<300 lx', '>=300 lx & <400 lx', '>=400 lx'});

xlabel('X-axis');
ylabel('Y-axis');
zlabel('Illuminance (lx)');
title('Surface Graphs');