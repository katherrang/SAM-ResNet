% visualizes SAM output as image overlay 

output_folder = 'example';  
showTitle = 1;  % 1 = yes, 0 = no
isMac = 0;      % 1 = yes, 0 = no 

% remove old overlay and summary files
overlayPath =  "overlay/" + output_folder;
if exist(overlayPath, 'dir')
    rmdir(overlayPath,'s')
end
mkdir(overlayPath);

summaryPath = "summary/" + output_folder;
if exist(summaryPath, 'dir')
    rmdir(summaryPath,'s')
end
mkdir(summaryPath);

% import image filenames
extractFilenames = dir("raw_output/" + output_folder + "/");
if isMac
    files = extractFilenames(4:end);
else
    files = extractFilenames(3:end);
end

for i=1:length(files)
    img = files(i).name;
    disp(img)
    
    % read original file
    [E, emap] = imread(strcat("original/", output_folder,"/",img));

    % read SAM output file
    I = imread(strcat("raw_output/", output_folder,"/",img));
    % convert output to heatmap coloring
    greyImage = ind2gray(I, gray);
    rgbImage = ind2rgb(greyImage, jet);
    
    % generate overlay image
    figure(1); clf
    imshow(E, emap, 'InitialMag', 'fit') % original image
    hold on
    h=imshow(rgbImage); % heatmap overlay
    hold off
    set(h, 'AlphaData', greyImage)
    colormap jet % colorbar
    caxis([0, 1])
    colorbar
    
    % save overlay image
    exportgraphics(gcf, strcat("overlay/", output_folder,"/",img))

    % generate summary image
    figure(2); clf
    t = tiledlayout(1,3);

    nexttile(t) % original image
    imshow(E, emap, 'InitialMag', 'fit') 
    title('Original')
 
    nexttile(t) % SAM output
    imshow(im2gray(I), 'InitialMag', 'fit') 
    title('SAM output')

    nexttile(t) % heatmap overlay
    imshow(E, emap, 'InitialMag', 'fit') % original image
    hold on
    h=imshow(rgbImage); % heatmap overlay
    hold off
    set(h, 'AlphaData', greyImage)
    colormap jet % colorbar
    caxis([0, 1])
    colorbar
    title('Overlay')

    % save summary image
    if showTitle == 1
        title(t,{img,''},'Interpreter','none')
    end
    exportgraphics(gcf, strcat("summary/", output_folder,"/",img))

end


