

### C language

#### 第一章:程序结构 

主要包括:预处理指令,函数,变量,语句&表示式, 注释

~~~ c
#include <stdio.h> // 预处理指令 C编译器编译之前要包含该文件

int main() {// 主函数
    printf("Hello, World!\n"); // 语句 表达式,函数
    return 0;//函数结束
}
~~~

#### 第二章:数据结构

c语言包含了基本类型(整数类型,浮点类型),枚举类型,void类型,派生类型(指针,数组,结构,共用体和函数类型)

~~~c
1.整数类型 char,unsigned-char,signed char, int,unsigned int, short, unsigned short, long,unsigned long
2.浮点型: float ,double,long double.
#include <stdio.h>
int main() {// 主函数
    printf("check datatype:%d\n", sizeof(int));// lu为32位无符号类型整数 查看当前数据(存储)类型占用字节大小
    printf("check datatype:%lu\n", sizeof(unsigned int ));
    printf("check datatype:%lu\n", sizeof(signed int));
    printf("check datatype:%E\n", sizeof(char)); //%E 为以指数形式输出单、双精度实数
    //444 4.940656E-324
    return 0;
}
~~~

#### 第三章: 变量和常量

变量声明向编译器保证变量以指定的类型和名称存在，这样编译器在不需要知道变量完整细节的情况下也能继续进一步的编译。变量声明只在编译时有它的意义，在程序连接时编译器需要实际的变量声明。

变量的声明由两种情况,一种需要建立存储空间,一种不需要,通过extern 声明变量而不进行定义

~~~c
#include <stdio.h>
int x, y,result;
int add_num(){
    // extern 是为了声明x,y 是全局变量.
    extern x;
    extern y;
    //给外部全局变量赋值;
    x=1;
    y=3;
    return x+y;
}
int main() {// 主函数
    result=add_num();
    printf("the add result:%d\n", result);
    return 0;
}
//4
~~~

常量定义:使用#define 预处理器定义/使用**const** 关键字

~~~c
#include <stdio.h>
//#define LENGTH 10 // define constant values.不指定类型,没有分号
//#define WIDTH 5
const int LENGTH=10; //type name=value;
const int WIDTH=5;
int main() {// 主函数
    int area = LENGTH * WIDTH;
    printf("the area is:%d",area);
    return 0;
}
~~~

#### 第四章:C 存储类

存储类定义 C 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。下面列出 C 程序中可用的存储类：

- **auto** 所有局部变量默认的存储类

- **register** 用于定义(可能)存储在寄存器中而不是RAM中的局部变量,变量的最大尺寸等于寄存器并且不能对他进行&运算 

- **static** 存储类指示编译器在程序的生命周期内保持局部变量的存在，而不需要在每次它进入和离开作用域时进行创建和销毁。因此，使用 static 修饰局部变量可以在函数调用之间保持局部变量的值。

  static 修饰符也可以应用于全局变量。当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。

  全局声明的一个 static 变量或方法可以被任何函数或方法调用，只要这些方法出现在跟 static 变量或方法同一个文件中

- **extern** 提供一个全局变量的引用对所有程序文件可见,

~~~c
#include <stdio.h>
static  int count =10; // 变量声明为static不会因为每次调用函数而重置变量值.变量是全局的 就是默认static
void func(void){
static num = 5; //在函数中定义静态变量.定义为非static 每次调用就是初始的结果6
num++;
printf("the count is:%d\t",count);
printf("the static num :%d\n", num);
}
int main() {// 主函数
while (count--){
    func();
}
return 0;
}
/**the count is:9  the static num :6
the count is:8  the static num :7
the count is:7  the static num :8
the count is:6  the static num :9
the count is:5  the static num :10
the count is:4  the static num :11
the count is:3  the static num :12
the count is:2  the static num :13
the count is:1  the static num :14
the count is:0  the static num :15**/
~~~

#### 第五章:运算符(算术,关系,逻辑,位,赋值,杂项(sizeof,&,*,?:))

~~~c
sizeof() 返回变量大小, &a;求变量的实际地址,*a;指针指向一个变量,?:;三目(条件表达式). 
   #include <stdio.h>
int main() {// 主函数
    int b=10;
    double a =3.145;
    int c = (b==10)?20:30; // 三目表达式
    printf("address%d\n",&c);// &a 给出变量的实际内存地址.
    printf("result:%d\n",c);
    return 0;
}
~~~

#### 第六章:C判断(if,switch,?:),循环(for,while,),

~~~c
#include <stdio.h>
// 判断
int main() {
    int num=10;
    if (num>20){
        printf("the num is %d\n",num);
        }
    else{
        printf("error:$$$");
    }
    }
#include <stdio.h>
// 循环
int main() {
    int count=10;
  for(int i=0;i<=count;i++){
      printf("the num is:%d\n",i);
  }
    }

~~~

#### 第七章:函数

~~~c
#include <stdio.h>
// 函数
int sum(int a, int b){
    return a+b;
}
int main() {
    int num1,num2,result;
    printf("enter integer num1:");
    scanf("%d",&num1);//变量的键盘输入
    printf("enter integer num2:");
    scanf("%d",&num2);
    result=sum(num1,num2);//函数的调用和传参
    printf("the result is:%d\n",result);
    return 0;
    }
~~~

#### 第八章:数组

~~~c
#include <stdio.h>
// 数组
int sum(int a, int b){
    return a+b;
}
int main() {
    int array[2]={10,30};//二位数组:int array[3][4]={0,0,0,0,}{0,0,0,0,}{0,0,0,0};
    int arrays[2][2]={{2,3},{1,2}};
    int result;
    result=sum(array[0],array[1]);
    printf("%d\n",result);
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            printf(":%d\n",arrays[i][j]);
        }
    }
    return 0;
    }

~~~

#### 第九章 enum枚举(enumerate列举)

~~~c
#include <stdio.h>
// 枚举
enum DAY{
    monday=1,tuesday,wednesday,thursday,friday,saturday,sunday
}day;

int main() {
    enum DAY day;
    day=tuesday;//2
    printf("%d\n",day);//2
    //如果枚举是连续的就可以进行循环遍历
    for(int day=monday;day<=sunday;day++){
        printf("the day is:%d\n",day);
    }
    return 0;
    }
/**2
the day is:1
the day is:2
the day is:3
the day is:4
the day is:5
the day is:6
the day is:7**/
~~~

#### 第十章:指针变量,指针函数

~~~c
#include <stdio.h>
// 指针:就是指向目标变量的地址的一个针,可以通过指针访问目的地址 进而使用值.
int main() {
    int num=100;
    int *p;
    p=&num;
    printf("num value:%d\n",num);//100
    printf("num address value:%p\n",&num);//000000000061FE14  指针里存着num地址
    printf("point value:%p\n",&p);//000000000061FE10 指针的内存地址号
    printf("point direction value:%d\n",*p);//100 指针指向地址的数据;
    return 0;
    }
// 指针遍历访问数组
#include <stdio.h>
int main() {
    int num[]={10,100,200,500,1000};
    int *ptr=num;// 指针指向数组
    for(int i=0;i<5;i++){
        printf("pointer address:var[%d]=%p\n",i,&ptr);// 指针指向数组的地址
        printf("pointer value:var[%d]=%d\n",i,*ptr);// 指向数组的值
        *ptr++;// 指向下一个位置
    }
    return 0;
    }
    /**
pointer address:var[0]=000000000061FDF8
pointer value:var[0]=10
pointer address:var[1]=000000000061FDF8
pointer value:var[1]=100
pointer address:var[2]=000000000061FDF8
pointer value:var[2]=200
pointer address:var[3]=000000000061FDF8
pointer value:var[3]=500
pointer address:var[4]=000000000061FDF8
pointer value:var[4]=1000
     **/
~~~


~~~c
//pointer function
#include <stdio.h>
// 指针函数 	
int max(int a,int b) {

    return a>b? a:b;
}
int main() {
    int a,b,c,d;
    printf("enter three numbers:");
    scanf("%d%d%d",&a,&b,&c);//scanf 赋值的时候需要&。
    int (*ptr)(int,int)=max;// 整形指针指向max有两个整型参数的函数
    d=ptr(ptr(a,b),c);//指针函数嵌套 参数分别是(a,b)c
    printf("the max is:%d\n",d);
    return 0;
    }
~~~

~~~c
/**
回调函数，指针作为函数的参数
**/

~~~



### opencv_C

#### reading  an image: loading, modify , output, store.

~~~~c
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

#### mask operation

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

