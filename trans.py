from PIL import Image
import glob
import sys
import os
from argparse import ArgumentParser

#引数をチェック
argparser = ArgumentParser()
argparser.add_argument("input_dir",type=str,help="Where to read files")
argparser.add_argument('-o','--output_dir',type=str,default="none",help="Where to output files:\n default is input_dir/result/")
argparser.add_argument('-n','--nameOutput',type=str,default="",help="The initial name for output images\n default is none")
argparser.add_argument('-w','--width',type=int,default=640,help="The width of transformed images:\n default is 640")
argv = argparser.parse_args()
input_dir = argv.input_dir
output_dir = argv.output_dir
initial_name = argv.nameOutput
width = argv.width
if output_dir == "none":
    output_dir = input_dir + "/result"
os.makedirs(output_dir,exist_ok=True)

#もし今のinitial_nameで出力した形跡があるなら確認を取る
if os.path.exists(output_dir+"/"+initial_name+str(0).zfill(3)+".png"):
    print("既に指定した出力ディレクトリ、initial_nameのファイルが存在します")
    print("構わず上書きをしてよい場合は'y'、やめる場合はそれ以外を入力してください")
    input_test_word = input('>>>  ')
    if str(input_test_word) != 'y':
        print("終了します")
        sys.exit()


#input_dirの全ファイルを取得
print(input_dir)
files = glob.glob(input_dir + "/*")

print(files)

#jpg,png,bmpファイルのみを取り出して新たにimgsに保管
imgs = []
no_imgs = []
for f in files:
    ext = f.split(".")[-1]
    if ext == "png" or ext == "jpg" or ext == "bmp":
        imgs.append(f)
    else:
        no_imgs.append(f)
imgs.sort()
img_l = len(imgs)
no_img_l = len(no_imgs)
print("以下の"+str(no_img_l)+"項目は画像ではないと判断されました")
for f in no_imgs:
    print(f.split("/")[-1])

print(str(img_l)+"画像ファイルを変換します")

#各画像を横640にして連番つけてoutput_dirに出力
i = 0
for img in imgs:
    image = Image.open(img)
    w, h = image.size
    per = 640.0 / w
    new_w = width
    new_h = int(h * per)
    image = image.resize((new_w,new_h),Image.LANCZOS)
    image.save(output_dir+"/"+initial_name+str(i).zfill(3)+".png")
    i+=1
    print(str(i)+"/"+str(img_l)+" 終了")

print("変換が終わりました！結果は\n"+output_dir+"\nに保存されています")