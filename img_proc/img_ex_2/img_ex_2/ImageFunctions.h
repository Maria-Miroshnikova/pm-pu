#pragma once
#include "BmpStructures.h"

RgbImg read_rgb_img(char const filename[]);
void write_rgb_img(char const filename[], RgbImg const& img);
void print_rgb_img_info(char const filename[]);
void delete_rgb_img(RgbImg& img);
RgbImg make_empty_rgb_img(RgbImg const& img);