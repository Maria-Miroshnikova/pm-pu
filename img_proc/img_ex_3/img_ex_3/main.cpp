#include <iostream>
#include "BmpStructures.h"
#include "ImageFunctions.h"

int comparer(const void* a, const void* b)
{
	return (*(int*)a - *(int*)b);
}

RGB filter_pixel(RgbImg const& img, int i, int j)
{
	const int countBoard = 9;
	RGB bluredPixel[countBoard];

	int index = 0;
	int index_result_pixel;

	for (int idx = i - 1; idx <= i + 1; ++idx)
	{
		for (int idy = j - 1; idy <= j + 1; ++idy)
		{
			if ((idy >= 0) && (idy < img.width) && (idx >= 0) && (idx < img.height))
			{
				bluredPixel[index] = img.pixels[idx][idy];
				if ((idx == i) && (idy == j))
					index_result_pixel = index;
				index++;
			}
		}
	}

	qsort(bluredPixel, index, sizeof(BYTE), comparer);

	return bluredPixel[index_result_pixel];
}

void median_filter(RgbImg const& img)
{
	RgbImg tmp_img = make_empty_rgb_img(img);

	for (int i = 0; i < img.height; ++i)
		for (int j = 0; j < img.width; ++j)
			tmp_img.pixels[i][j] = filter_pixel(img, i, j);

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

		median_filter(img);

		write_rgb_img("coloredout.bmp", img);

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