

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

c语言包含了基本类型(整数类型,浮点类型),枚举类型,void类型,派生类型(指针,数组,结构,共用体和函数类型) +类型转换

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

#### 第十章:指针变量,指针函数,回调函数

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
#include<stdio.h>
#include <cstdlib>
//回调函数
void get_array(int *array, size_t array_size,int (*random_)()){
    for (int i=0;i<array_size;i++){
        array[i]=random_();//random_()函数得到的值传到数组中
    }
}
// random values.
int random_(){
    return rand();
}
int main() {
    int array[10];//define an array to accept values.
    get_array(array,10,random_);//第一个参数是指针变量，第二个参数是数组大小，第三个参数是回调函数。
    //遍历输出
    for(int i=0;i<10;i++){
        printf("print array values:i=[%d]%d\n",i,array[i]);
    }
    return 0;
}

~~~

#### 第十一章：字符串

字符串函数：

~~~c
#include <cstdio>
#include<cstring>
int main(){
    char array_ch[10]={'a','r','r','a','y'};//创建一个字符串数组 这里的10对于连接字符串很重要
    char ch_array[]="print";//不同初始化的字符数组
    //strcpy(array_ch,ch_array);// s2 to s1 数组  输出结果 print.
    //strcat(array_ch,ch_array);//连接两个字符串为一个数组，s1+s2 arrayprint 给输出数组指定空间
    int len =strlen(array_ch);//字符串长度
    int boo=strcmp(array_ch,ch_array);//匹配两个字符串 相同返回0，s1<s2 小于0 否则大于0
    strchr(array_ch,'a');//返回一个指针 指向第一个出现s2的位置
    strstr(array_ch,ch_array);//返回一个指针，指向S1中第一次出现S2的位置
    printf("%d\n",boo);
    printf("print array_char:");
    for(char i:array_ch){//循环遍历数组 这里使用了rang 值循环
        printf("%c",i);
    }
}
~~~

#### 第十二章：结构体

**结构**是 C 编程中另一种用户自定义的可用的数据类型，它允许您存储不同类型的数据项。

~~~c
#include "cstdio"
#include "cstring"
struct books{ // 结构名
    char title[50];
    char author[20];
    char subject[50];
    int book_id;
}book={"c language","gary","c learning",123456};//结构体内容的初始化 这里没有内容可以在函数中进行声明成员
// 结构没有初始化，后续进行声明 struct books book1; 然后可以使用成员 book1
int main(){
    strcpy(book.title,"java");// 通过结构的成员变量进行访问 覆盖了title的数组内容
    printf("title:%s\nauthor:%s\nsubject:%s\nbook_id:%d",book.title,book.author,book.subject,book.book_id);
    return 0;
}
//结构作为函数的参数demo
#include "cstdio"
#include "cstring"
struct BOOKS{ // 结构名
    char title[50];
    char author[20];
    char subject[50];
    int book_id;
};
//结构作为了函数的参数 函数也可以先声明
void struct_print(BOOKS book){
    printf("title:%s\nauthor:%s\nsubject:%s\nid:%d",book.title,book.author,book.subject,book.book_id);
}
int main(){
    //对结构进行初始化
    struct BOOKS book1;// 声明成员book1 类型是BOOKS
    strcpy(book1.title,"c language");
    strcpy(book1.author,"gary");
    strcpy(book1.subject,"c programming");
    book1.book_id=123456;
    struct_print(book1);
    return 0;
}
//定义指向结构的指针，可以 通过指针进行访问结构
#include "cstdio"
#include "cstring"
struct BOOKS{ // 结构名
    char title[50];
    char author[20];
    char subject[50];
    int book_id;
};
void struct_print(BOOKS *book){// 定义了指向成员的指针 在使用属性内容时不再是单独的DOC要改变-> 指向成员的属性
    printf("title:%s\nauthor:%s\nsubject:%s\nid:%d",book->title,book->author,book->subject,book->book_id);
}
int main(){
    //对结构进行初始化
    struct BOOKS book1;// 声明成员book1 类型是BOOKS
    strcpy(book1.title,"c language");
    strcpy(book1.author,"gary");
    strcpy(book1.subject,"c programming");
    book1.book_id=123456;
    struct_print(&book1);// 这里要使用&符号 表明地址身份
    return 0;
}
~~~

#### 十三章:位域/位段

带有预定义宽度的变量被称为**位域**。位域可以存储多于 1 位的数，例如，需要一个变量来存储从 0 到 7 的值，您可以定义一个宽度为 3 位的位域

~~~c
#include"cstdio"
#include"cstring"
/**
 *
 * @gary
 * 位域的演示
 */
struct Bit{// 定义位域结构 告诉编译器只使用指定的位。如果超出了就到达下一个位空间
    //unsigned int bit_width:1;// 指定创建的位空间大小,如果没有指定两个整形占一个字节，就占8位，这里两个整形指定一位 所以大小是4.
    //unsigned int bit_height:1;
    unsigned int age:2;//实例 指定年龄的位域 0-3 00-11
}bit;
int main(){
    bit.age=4;//指定数字就是占位数 必须在指定位之内的值。
    printf("the width of bit:%d\n",sizeof(bit));//结果是4,因为指定了位空间1 占一个字节 四位。1111
    printf("the age is:%d\n",bit.age);
    return 0;
}
~~~

#### 第十四章:共用体

共用体是一种特殊的数据类型，允许您在相同的内存位置存储不同的数据类型。您可以定义一个带有多成员的共用体，但是任何时候只能有一个成员带有值。共用体提供了一种使用相同的内存位置的有效方式。

~~~C
#include "stdio.h"
#include"string.h"
// 共用体demo 优势是我们不用开辟更多的空间用于存放变量值,我们值需要开辟一个空间,定义不同的成员,进行更新使用就可以了.
union Data{
    int i;
    float j;
    char name[20]; // 最大的空间作为共用体的空间,内存空间同一时间只能给一个变量使用.
}data;
int main(){
    // 可以分别使用共用体,但是同一时间读取内容的时候就会出现问题.
    strcpy(data.name,"gary");//第一次对该空间进行赋值
    data.i=100;//第二次覆盖赋值
    printf("%d\n",data.i);//显示最新值
    printf("%s\n",data.name);// 这里显示的应该是100 但是因为类型不同 显示不是Gary 也不是100 可能是100在ASCII的字符
    return 0;
}

~~~

#### 第十五章：typedef 

 typedef 和#define的区别：

**#define** 是 C 指令，用于为各种数据类型定义别名，与 **typedef** 类似，但是它们有以下几点不同：

- **typedef** 仅限于为类型定义符号名称，**#define** 不仅可以为类型定义别名，也能为数值定义别名，比如您可以定义 1 为 ONE。
- **typedef** 是由编译器执行解释的，**#define** 语句是由预编译器进行处理的。

~~~c
#include "cstdio"
#include"cstring"
/**
 *
 * @gary
 * typedef 的使用和#define的区分
 */
typedef struct Books{// typedef 为结构取新的名字
    char title[50];
    char name[20];
    char author[20];
    int book_id;
}book;
int main(){
    typedef int zx;//给整形取了一个新的名字 zx 在后边可以替代使用 特别是自己定义的数据结构很方便
    zx value=10;
    printf("%d\n",value);//10
    // 结构的TYPEDEF
    book book1;// 因为结构进行了重命名声明，我们进行了重命名 book1 使用 book 已经不好使了。
    strcpy(book1.title,"c language");
    printf("print title:%s\n",book1.title);
    return 0;
}
~~~

#### 第十六章：input,output

printf() 来自于dtdio.h库的输出函数。 getchar(),putchar()  gets(),puts(),

~~~c
#include "cstdio"
#include "cstring"
int main(){
//    printf("enter character:");
//    int c=getchar();//输入字符 返回值是一个整数值
//    printf("print character:");
//    putchar(c);//一次输出一个字符 Only
    // gets() puts() 函数 读取一行字符串到指向的缓冲区 直到一个中指符/EOF
    char str[100];
    printf("enter:");
    gets(str);
    printf("\nprint:");
    puts(str);
// scanf() and printf()
    return 0;
}
~~~

#### 第十七章：文件读写

r: 打开一个已有的文本文件，允许读取文件

w: 打开一个文本文件，允许写入文件。如果文件不存在，则会创建一个新文件。在这里，您的程序会从文件的开头写入内容。如果文件存在，则该会被截断为零长度，重新写入。

a:打开一个文本文件，以追加模式写入文件。如果文件不存在，则会创建一个新文件。在这里，您的程序会在已有的文件内容中追加内容

r+:打开一个文本文件， 允许读写文件

w+:打开一个文本文件，允许读写文件。如果文件已存在，则文件会被截断为零长度，如果文件不存在，则会创建一个新文件。

a+:打开一个文本文件，允许读写文件。如果文件不存在，则会创建一个新文件。读取会从文件的开头开始，写入则只能是追加模式。

如果处理的是二进制文件，"rb", "wb", "ab", "rb+", "r+b", "wb+", "w+b", "ab+", "a+b"

~~~c
/**
 * 文件读写
 * @gary
**/
#include "cstdio"
#include "cstring"

int main(){
//    FILE *fp=NULL;// 空指针 类型FILE包含了所有用来控制流的必要信息
//    fp = fopen("E:/CL/open.txt","w+");
//    fprintf(fp,"this is file print message,");//文档输入
//    fputs("this is puts message.",fp);//输入
//    fclose(fp);// close file .
    // read file
    FILE *fp=NULL;
    char buff[500];
    fp = fopen("E:/CL/open.txt","r");
    //fscanf(fp,"%s\n",buff);//fscanf()遇到第一个空格和换行符停止
    //printf("the result is:%s\n",buff);
    printf("-------------\n");
    fgets(buff,200,(FILE*)fp);// 读取n-1个字符 最后n是追加的终止符
    printf("the file is:%s\n",buff);
    fclose(fp);
    // binary I/O function:
    
    return 0;

}
~~~

#### 第十八章：C预处理器

~~~c
/**C 
预处理器不是编译器的组成部分，但是它是编译过程中一个单独的步骤。简言之，C 预处理器只不过是一个文本替换工具而已，它们会指示编译器在实际编译之前完成所需的预处理。我们将把 C 预处理器（C Preprocessor）简写为 CPP。
所有的预处理器命令都是以井号（#）开头。它必须是第一个非空字符，为了增强可读性，预处理器指令应从第一列开始。下面列出了所有重要的预处理器指令：
#define	定义宏
#include 包含一个源代码文件
#undef	取消已定义的宏
#ifdef	如果宏已经定义，则返回真
#ifndef	如果宏没有定义，则返回真
#if	如果给定条件为真，则编译下面代码
#else	#if 的替代方案
#elif	如果前面的 #if 给定条件不为真，当前条件为真，则编译下面代码
#endif	结束一个 #if……#else 条件编译块
#error	当遇到标准错误时，输出错误消息
#pragma	使用标准化方法，向编译器发布特殊的命令到编译器中
**/
~~~

#### 第十九章：C头文件：

~~~c
/**
头文件是扩展名为 .h 的文件，包含了 C 函数声明和宏定义，被多个源文件中引用共享。有两种类型的头文件：程序员编写的头文件和编译器自带的头文件。

在程序中要使用头文件，需要使用 C 预处理指令 #include 来引用它。前面我们已经看过 stdio.h 头文件，它是编译器自带的头文件。

引用头文件相当于复制头文件的内容，但是我们不会直接在源文件中复制头文件的内容，因为这么做很容易出错，特别在程序是由多个源文件组成的时候。

A simple practice in C 或 C++ 程序中，建议把所有的常量、宏、系统全局变量和函数原型写在头文件中，在需要的时候随时引用这些头文件。
**/
~~~

#### 第二十章：错误处理：

~~~c
/**
C 语言不提供对错误处理的直接支持，但是作为一种系统编程语言，它以返回值的形式允许您访问底层数据。在发生错误时，大多数的 C 或 UNIX 函数调用返回 1 或 NULL，同时会设置一个错误代码 errno，该错误代码是全局变量，表示在函数调用期间发生了错误。您可以在 errno.h 头文件中找到各种各样的错误代码。

所以，C 程序员可以通过检查返回值，然后根据返回值决定采取哪种适当的动作。开发人员应该在程序初始化时，把 errno 设置为 0，这是一种良好的编程习惯。0 值表示程序中没有错误。
**/
#include "cstdio"
#include "cstring"
#include "cerrno"
/**
 * C 语言提供了 perror() 和 strerror() 函数来显示与 errno 相关的文本消息。
**/
extern int errno;
int main(){
    FILE *fp;
    int errnum;
    fp=fopen("un_exist.txt","rb");
    if (fp == NULL){
        // 两种错误显示方式：
        errnum = errno;
        fprintf(stderr,"wrong num:%d\n",errno);//stderr 文件流输出错误

        perror("perror print error");//这两句结果一致
        fprintf(stderr,"file opened wrong:%s\n",strerror(errnum));//
    }else{
        fclose(fp);
    }
    return 0;
}
~~~

#### 第二十一章：recursion 递归

~~~c
#include "cstdio"
#include "cstring"
#include "cerrno"
/**
 * C 语言的递归调用  演示裴波那契数列
**/
int recursion(int i){
    if(i==0){
        return 0;
    }
    if(i==1){
        return 1;
    }
    return recursion(i-1)+recursion(i-2);

}
int main(){
    int i;
    for(i=0;i<10;i++){
        printf("the sequence are:%d\n",recursion(i));
    }
    return 0;
}
//0 1 1 2 3 5 8 13 21 34
~~~

#### 第二十二章：C可变参数：

~~~c

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

