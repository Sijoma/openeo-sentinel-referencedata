from sentinelsat import SentinelAPI
from sys import argv
import logging

logging.basicConfig(format='%(message)s', level='INFO')

def download_products(targetfolder, user, password):
	api = SentinelAPI(user, password)
	print('Connected')
	products = []
	with open('uids.txt','r') as uids:
		for uid in uids:
			products.append(uid.strip())
	api.download_all(products, directory_path = targetfolder)
	print("Downloaded " + str(len(products)) + " product(s).")


if __name__ == "__main__":
	# CLI arguments: targetfolder, user, password)
	download_products(argv[1], argv[2], argv[3])
