import zipfile
import py7zr
sifre_listesi = input("Sifrelerin oldugu dosyayi giriniz: ")
kirilacak_dosya = input("Kirilacak dosyayi giriniz: ")

try:
	def picklock(obj):
		with open(sifre_listesi, "rb") as veri:
			for diziler in veri:
				for kelime in diziler.split():
					try:
						obj.extractall(pwd=kelime)
						print("Sifre: ", kelime.decode())
						return True
					except:
						continue
		return False


	dosya = zipfile.ZipFile(kirilacak_dosya)

	deneme_sayimi = len(list(open(sifre_listesi, "rb")))

	print(deneme_sayimi, " sifre test edildi.")

	if picklock(dosya) == False:
		print("Sifre bulunamamawk")

except:
	print("Hatali girmissin kardsm")

