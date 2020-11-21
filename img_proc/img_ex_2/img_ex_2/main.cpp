#include <iostream>
#include "BmpStructures.h"
#include "ImageFunctions.h"

RGB filter_pixel(RgbImg const& img, int i, int j, int n)
{
	RGB bluredPixel = { 0, 0, 0 };
	int rgb[3] = { 0, 0, 0 };
	int count = 0;

	for (int idx = i - n; idx <= i + n; ++idx)
	{
		for (int idy = j - n; idy <= j + n; ++idy)
		{
			//if ((idx == i) && (idy == j)) // ne uchitivat` current pixel?
			//	continue;
			if ((idy >= 0) && (idy < img.width) && (idx >= 0) && (idx < img.height))
			{
				rgb[0] += img.pixels[idx][idy].Red;
				rgb[1] += img.pixels[idx][idy].Green;
				rgb[2] += img.pixels[idx][idy].Blue;
				count++;
			}
		}
	}

	bluredPixel.Red = rgb[0] / count;
	bluredPixel.Green = rgb[1] / count;
	bluredPixel.Blue = rgb[2] / count;

	return bluredPixel;
}

void window_filter(RgbImg const& img, int n)
{
	RgbImg tmp_img = make_empty_rgb_img(img);

	for (int i = 0; i < img.height; ++i)
		for (int j = 0; j < img.width; ++j)
			tmp_img.pixels[i][j] = filter_pixel(img, i, j, n);
	
	for (int i = 0; i < img.height; ++i)
		for (int j = 0; j < img.width; ++j)
			img.pixels[i][j] = tmp_img.pixels[i][j];

	delete_rgb_img(tmp_img);
}

int main()
{
	try
	{
		RgbImg img = read_rgb_img("colored.bmp");

		window_filter(img, 6);

		write_rgb_img("col_out_central_6.bmp", img);

		delete_rgb_img(img);
	}
	catch (std::exception error)
	{
		std::cout << "Error happened: " << error.what() << '\n';
		return 1;
	}
	std::cout << "Success!\n";
	return 0;
}