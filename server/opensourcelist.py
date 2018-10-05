import json

class OpenSourceSoftware:

    def __init__(self):
        self.OpenSourceSoftware = []

    def add_OpenSourceSoftware(self, name, short_description, site):
        new_oss = {}
        new_oss["name"] = name
        new_oss["short_desciption"] = short_description
        new_oss["site"] = site
        self.OpenSourceSoftware.append(new_oss)

    def delete_OpenSourceSoftware(self, name):
        found = False
        for i, oss_entry in enumerate(self.OpenSourceSoftware):
            if oss_entry["name"] == name:
                index = i
                found = True
                del self.OpenSourceSoftware[i]
        # print("name: {0}".format(json.dumps(self.OpenSourceSoftware)))
        return found

    def list(self):
        return self.OpenSourceSoftware

    def json_list(self):
        return json.dumps(self.OpenSourceSoftware)

if __name__ == "__main__":
    oss = OpenSourceSoftware()
    oss.add_OpenSourceSoftware(name = "OpenSSL", short_description="OpenSSL Package", site = "https://www.openssl.org")
    oss.add_OpenSourceSoftware(short_description="SSH Package", site = "https://www.openssh.org", name="openssh")
    print (oss.json_list())
    oss.delete_OpenSourceSoftware(name="OpenSSL")
    print ("after delete")
    print (oss.json_list())
