### reading  an image: loading, modify , output, store.

~~~c
#include<opencv2/opencv.hpp>
using namespace cv;  // 使用命名空间进行指定, 在代码中可以省略
int main(int argc, char** argv) {
	// mat 是一个图像参数对象
	// <0 表示加载原图像, =0 灰度图  >0 原图作为RGB加载  或者写代码
	//img = imread("E:/python_OpenCV lib/lena.jpg", IMREAD_UNCHANGED);
	//img = imread("E:/python_OpenCV lib/lena.jpg",IMREAD_GRAYSCALE );
	//img = imread("E:/python_OpenCV lib/lena.jpg", IMREAD_COLOR);
	Mat img = imread("E:/python_OpenCV lib/lena.jpg", -1);// BMP, DIB, JPEG, PNG, PBM, PGM, PPM ,ST, RAS, TIFF.

	if (img.empty()) {
		printf("could not find image...\n");
		return -1;
	}
	Mat img_cvtcolor;  // 创建一个色彩转换对象
	//cvtColor(img, img_cvtcolor, COLOR_BGR2GRAY);  //色彩转换操作
	cvtColor(img, img_cvtcolor, COLOR_BGR2HLS);// 以我的代码为准 不再是CV_BGR2HLS

	// 保存结果图像
	imwrite("E:/python_OpenCV lib/lena_cHLS.jpg", img_cvtcolor);

	namedWindow("example",WINDOW_AUTOSIZE);// 创建一个窗口 自动创建和释放 无需销毁
	imshow("example", img);
	//显示色彩转换为HSI的结果
	namedWindow("cvt_res", WINDOW_AUTOSIZE);
	imshow("cvt_res", img_cvtcolor);
	waitKey(0);
	destroyWindow("example");
	destroyWindow("cvt_res");
	return 0;
}
~~~

### mask operation

~~~c++
//E:/python_OpenCV lib/lena.jpg
// 矩阵的掩模操作: 获取图像像素指针, 
#include<opencv2/opencv.hpp>
#include<iostream>
#include<math.h>
using namespace cv;

int main(int argc, char** argv) {
	Mat dst, img= imread("E:/python_OpenCV lib/lena.jpg");//定义了两个对象 img, 和dst
	if (!img.data) {// 如果img.data 为false 那么返回-1 没有找到图像
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("res", WINDOW_AUTOSIZE);// 
	imshow("res", img); // 显示图像
	// mask operation  掩码操作 或者叫做kernel, 卷积核
	/*int cols = (img.cols - 1) * img.channels();
	int offsetx = img.channels();
	int rows = img.rows;
	dst = Mat::zeros(img.size(), img.type());// 创建一个和原图像大小相等,类型相同用0填充的图像. dst
	*/
	//进行卷积 
	// 我们直接使用API进行操作 这里的两步函数调用,直接代替了以上的代码
	double t = getTickCount();
	Mat kernel = (Mat_<char>(3,3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
	filter2D(img, dst, img.depth(), kernel);
	double timeconsume = (getTickCount() - t) / getTickFrequency();//计算消耗时间;
	printf("time consume: %.2f\n", timeconsume);//得出结果
	/*for (int row = 1; row < (rows - 1);row++) {
		const uchar* previous = img.ptr<uchar>(row - 1);
		const uchar* current = img.ptr<uchar>(row);
		const uchar* next = img.ptr<uchar>(row + 1);
		uchar* output = dst.ptr<uchar>(row);
		for (int col = offsetx; col < cols; col++) {
			output[col] = saturate_cast<uchar>(5 * current[col] - (current[col - offsetx] + current[col + offsetx] + previous[col] + next[col]));

		}
	}*/
	namedWindow("result", WINDOW_AUTOSIZE);
	imshow("result", dst);
	waitKey(0);
	destroyAllWindows;
	return 0;

}
~~~

