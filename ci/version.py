import sys

productName = 'AutoDeployer'
productVersion = '1.5'


if __name__ == "__main__":
    if len(sys.argv) > 1:
        param = sys.argv[1]

        if param == 'version':
            print(productVersion)
        elif param == 'name':
            print(productName)
        elif param == 'both':
            print(productName + '-' + productVersion)
        else:
            print('available value: version, name, both')