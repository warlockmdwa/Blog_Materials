import zipfile
from tqdm import tqdm


def main():
	sifre_listesi = input("Sifrelerin oldugu dosyayi giriniz: ")
	kirilacak_dosya = input("Kirilacak dosyayi giriniz: ")

	denemeler = len(list(open(sifre_listesi, "rb")))
	dosya = zipfile.ZipFile(kirilacak_dosya)

	with open(sifre_listesi, "rb") as veri:
		for diziler in tqdm(veri, total=denemeler):
			try:
				dosya.extractall(pwd=diziler.strip())
				sonuc = str(diziler.decode().strip())
				print("Sifre: "+sonuc)
			except:
				continue

	f = open("sifrelog.txt", "a+")

	f.write("Kaydedilen sifre: " + sonuc +" \n")
	f.close()

	print(denemeler, " sifre test edildi.")


if __name__ == '__main__':
	main()
