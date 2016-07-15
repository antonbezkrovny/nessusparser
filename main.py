from nessmanager import ScannerConnector

nessus_url="https://10.5.54.10:8834"
nessus_login="a-bezkrovny"
nessus_password="U-e.mx60"
nessus_nossl=True

NessusConnector = ScannerConnector(url=nessus_url, login=nessus_login,
                                   pwd=nessus_password, no_ssl=nessus_nossl)

point = NessusConnector.connect()
point.action(action="scans", method="get")
point.scan_id=1026
file = point.download_scan(export_format="nessus")
print(file)









