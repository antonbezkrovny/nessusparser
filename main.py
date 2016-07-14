from nessrest import ness6rest
import io
userpassword=input('Enter paswword for Nesssus: ')
scanner = ness6rest.Scanner(url="https://10.5.54.10:8834", login="a-bezkrovny", password=userpassword, insecure=True)
scanner.action(action="scans", method="get")
scanner.scan_id = 1026
with io.open('D:\\github\\nessusparser\\tmpscan.tmp', 'wt') as fp:
    fp.write(scanner.download_scan(export_format="nessus"))



