
import pdb
import pandas as pd


data = [
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyGXP3NHQ-w280-h280/asus-vivobook-16x-k3.webp",
        "productName": "Asus Vivobook 16X K3605ZF-MBN545WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB RTX2050)",
        "price": "₹69,990",
        "rating": "4.6",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqEaA1D3xjA5dGHhrhArnrysuhyihDRPKXReXb4oh-hrhhaFhrhrhhacBrWahrhrBi5PGoFogCAhrFB5KVP_Q84DiaOu"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieUw4VMBj-w280-h280/asus-vivobook-16x-k3.webp",
        "productName": "Asus Vivobook 16X K3605ZC-MBN554WS Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 4GB RTX3050)",
        "price": "₹74,990",
        "rating": "4.05",
        "specScore": "71",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFJ-6xJ0xobXCJhrhArnrysuhyihDRPKXRe5dVdh-hrhhaFhrhrhhacBrWahrhrBi5ln4yiOo3hrFB5BySWnO4g1Dy9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZ38vSz28-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JF002JIN Laptop (AMD Ryzen 3 7330U/ 8 GB/ 512 GB SSD/ Win11)",
        "price": "₹28,660",
        "rating": "4.2",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 3 7330U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQaXtP9WBSXiiC6hrhAgTYBOr3Uh7Taus2scrnic3IyaucZcNCricAs3acGZZPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacUtYuO6ssOc54cW4cUtYucTYWtUcTrBUshDhDh8b4lZbio5GagXrhmBYihkwkp7zXo_ldfJe_~GhrhhaFhrhrhhacBrWahrhrBi5nn5YGYlnhrFB55oNqXa1i-P6d"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJd2TTEJp-w280-h280/hp-victus-15-fa1351t.webp",
        "productName": "HP Victus 15-fa1351TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ RTX 2050)",
        "price": "₹57,990",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYxYwbvp8rSFJ.4hrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54cgr5Z45UDcWrnhNcTrBUshDhDh8lribbHlrga555hmBYihkwkpSfXV0dpEoe4~~hrhhaFhrhrhhacBrWahrhrBi5nFPW3i8UhrFB5kT6durVPze1I"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioXEIfxVI-w280-h280/acer-one-14-z8-415-l.webp",
        "productName": "Acer One 14 Z8-415 Laptop (11th Gen Core i3 / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹24,990",
        "rating": "4.05",
        "specScore": "54",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "‎Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzfCf8S1wV6mSK8hrhAgTYBOr3Uh7rAa3chFcoPoHcYuUaTcAs3acYZc55UtcWauc5554WHcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacrsc5HcycXcH54cUtYucTYWtUcTrBUshDhDh8ZHgoHA6rAbgobhmBYihkwkp71x4w~G0KJKzHhrhhaFhrhrhhacBrWahrhrBi5bHDHANWFhrFB5PqYXqV5ZKnvx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVmeTtYrm-w280-h280/lenovo-v15-g4-83cr00.webp",
        "productName": "Lenovo V15 G4 ‎83CR000VIN Laptop ( AMD Ryzen 7 7730U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹39,999",
        "rating": "4.5",
        "specScore": "63",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQO6btQP8yPAZ-KhrhAgTYBOr3Uh7Taus2sc254cgticrnic3IyaucGcsAUrcAs3acGGZPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacWHc6CFYuaFFcTrBUshDhDh8bibAgibbH4HXihmBYihkwkp7._S~.~1~ovXKhrhhaFhrhrhhacBrWahrhrBi5YXUTu35AhrFB5jCnnjYDi2Ix0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieKdtNl7s-w280-h280/hp-victus-15-fa0333t.webp",
        "productName": "HP Victus 15-fa0333TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB RTX 3050)",
        "price": "₹66,990",
        "rating": "4.2",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwu_S~G~JY.kU-NhrhArnrysuhyihDRPKXfJm5xvh-hrhhaFhrhrhhacBrWahrhrBi5u3nY5FTZhrFB5eXvCv2mZq9QQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHPqZ1yAb-w280-h280/dell-vostro-3520-lap.webp",
        "productName": "Dell Vostro 3520 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹33,890",
        "rating": "4.05",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYo4K4ZEFsYVsw1hrhAgTYBOr3Uh7iaTTc2sFU3scYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacZ4oPcUtYucTYWtUcTrBUshDhDh84ibloab54AlGahmBYihkwkpSoxoo_J1GK~xphrhhaFhrhrhhacBrWahrhrBi5bCIXItHXhrFB50nCk5IQS1exk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikJZDvo4T-w280-h280/hp-victus-15-fa1327t.webp",
        "productName": "HP Victus 15-fa1327TX Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX3050 Graph)",
        "price": "₹74,990",
        "rating": "4.4",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY~Xp9vkj1xFnxDhrhAgTYBOr3Uh7tBc2YAUCFc54coPoHcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgr5ZoGUDcWrnhNcTrBUshDhDh86PXg54Hgob4iGhmBYihkwkpSfXV0.GZfl11fhrhhaFhrhrhhacBrWahrhrBi5WOlWZnYNhrFB5z2TgVIip7U1w"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAgVQg4Xs-w280-h280/hp-15s-fq5326tu-lapt.webp",
        "productName": "HP 15s-fq5326TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹35,890",
        "rating": "4.55",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFxOuFgWusuAHg8hrhAgTYBOr3Uh7tBcgNcFa3YaFcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgN4ZobUCcTrBUshDhDh8alro4ZoPHZiAohmBYihkwkpSx7bZRvx07_SJhrhhaFhrhrhhacBrWahrhrBi5yClFNraQhrFB5Ofd4-wdgERQR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3lWoUzaO-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-76G UN.QMYSI.002 Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹53,990",
        "rating": "4.55",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF~gKUA6q8G0SyJhrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrG54cGbWc4otHcrG54cGbWcWrnhNcTrBUshDhDh8H4griPAolPoH4hmBYihkwkp7vS-EwffbZSjjhrhhaFhrhrhhacBrWahrhrBi5yoPNoYHThrFB5OvYBPqpnWlqS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itfXAOD2v-w280-h280/dell-15-g15-5530-gam.webp",
        "productName": "Dell 15 G15-5530 Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹80,390",
        "rating": "4.05",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw8kwRirSbvGmAGhrhArnrysuhyihDRPwvV_K_XZh-hrhhaFhrhrhhacBrWahrhrBi5ilI833nWhrFB5p_A4W3osnERj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imCxSargW-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ541WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹51,990",
        "rating": "4.7",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwgdrks_antazSahrhArnrysuhyihDRPwGSbeewXh-hrhhaFhrhrhhacBrWahrhrBi5P6iHY6a4hrFB5NwJWiRivyX-_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuyE8KL7Z-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83EM008GIN Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹63,990",
        "rating": "4.6",
        "specScore": "56",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwnjyCU8Y1VnYCkhrhArnrysuhyihDRPKbdw0~.~h-hrhhaFhrhrhhacBrWahrhrBi5GXZiG4gghrFB59kErBmQ7Kklt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXMsgRkkm-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2020 MGND3HN Laptop (Apple M1/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹67,990",
        "rating": "4.6",
        "specScore": "43",
        "features": [
            "Apple M1",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Apple M1 Integrated Graphics",
            "13.3 inches, 2560 x 1600 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90iruVfByHBATePhrhAgTYBOr3Uh7rBBTacoPoPcnrA6ssOcrY3cn5cXcW6co4bcW6cFFicnrAcsFc6YWcFC3cnWubZtucrh-hDh8ZAXGoglabG6AbhmBYihkwkpx_qVp7dS.fxSlhrhhaFhrhrhhacBrWahrhrBi5NABi4WQbhrFB5eka9uPf-2FaD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXYmi3ng-w280-h280/msi-thin-15-b12ucx-1.webp",
        "productName": "MSI Thin 15 B12UCX-1695IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX 2050 Graph)",
        "price": "₹53,700",
        "rating": "4",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmDPBmIEGrYXQDhrhArnrysuhyihDRPw0lel0zKh-hrhhaFhrhrhhacBrWahrhrBi5b5iyIDllhrFB5XUYA3TDKJOHe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifHKwQY9N-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-71 NX.KF1SI.0023 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4.7",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ25lTVE.8jHPVxhrhAgTYBOr3Uh7rAa3cF8YgUcWsc5Hca2scsTaicoPoHcYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFgW5HcG5c4XC6cUtYucTYWtUcTrBUshDhDh8PrPXP5lHibii5hmBYihkwkp7.V77jS.RjZJfhrhhaFhrhrhhacBrWahrhrBi5nQnDYQW4hrFB5Aq~rVVP2ZEDC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iiUG50dPR-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA506NCR-HN075WS Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹75,990",
        "rating": "4.7",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3ktAKO3Nf3Xl~DhrhAA3snrh7rFCFcUCgcWrnhNcr54crnic3IyaucGcWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAactsnachYcFUCiauUcW3rBthschncocZcOWch-hDZPXZP5hrhhaFhrhrhhacBrWahrhrBi5UP2643Z5hrFB5dDoH.II-VzH4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipKE8TXXF-w280-h280/red-magic-titan-16-p.webp",
        "productName": "Red Magic Titan 16 Pro Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ RTX 4060)",
        "price": "₹1,20,999",
        "rating": "4.3",
        "specScore": "77",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DRed%2520Magic%2520Titan%252016%2520Pro%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252016GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%2520RTX%25204060)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ietbDRCeQ-w280-h280/lenovo-loq-2024-83gs.webp",
        "productName": "Lenovo LOQ 2024 83GS003NIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX 3050 Graph)",
        "price": "₹70,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwNt879K~lOFKyfhrhArnrysuhyihDRPKHlvdZ_bh-hrhhaFhrhrhhacBrWahrhrBi5NblYoAn8hrFB5gG.jWnXvGl48"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKN69soSG-w280-h280/hp-victus-15-fa1226t.webp",
        "productName": "HP Victus 15-fa1226TX Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹55,490",
        "rating": "4.15",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpnK9mz2kmSfUVhrhArnrysuhyihDRPKoK7zp7eh-hrhhaFhrhrhhacBrWahrhrBi5AN2aBXuahrFB5v1~18TZY78ig"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i56bziHOT-w280-h280/msi-thin-a15-ai-b7uc.webp",
        "productName": "MSI Thin A15 AI B7UCX-068IN Gaming Laptop (AMD Ryzen 5 7535H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹56,990",
        "rating": "4",
        "specScore": "69",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz3E~lr-9bV-oHbhrhAgTYBOr3Uh7nFYcUtYucr54crnic3Iyauc4ctaDrcAs3acG4Z4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc6GCADcPbXYucWrnhNcTrBUshDhDh8ibagGgXAgZGbXhmBYihkwkp7_pe_.zjXdVz1hrhhaFhrhrhhacBrWahrhrBi5GYyyH4WWhrFB58rAg4kiOXSRF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iunkFSjxh-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JF002PIN Laptop (AMD Ryzen 5 7530U/ 8GB/ 512 GB SSD/ Win11)",
        "price": "₹37,990",
        "rating": "4.05",
        "specScore": "64",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzWjH9biJQS4SpwhrhAgTYBOr3Uh7Taus2scUtYuO6ssOc54cW4crnic3Iyauc4ctaDrcAs3acG4ZPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacUtYuOc6ssOcr6BcocUtYucTYWtUcTrBUshDhDh8gPHGrHGGHb4AAhmBYihkwkp7fVjR~KX-ow-HhrhhaFhrhrhhacBrWahrhrBi5P4C523AIhrFB54JVzaIf4Uzq9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJavk42Bg-w280-h280/hp-victus-15-fb0150a.webp",
        "productName": "HP Victus 15-fb0150AX Gaming Laptop (AMD Ryzen 5 5600H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹53,999",
        "rating": "4.15",
        "specScore": "68",
        "features": [
            "5th Gen AMD Ryzen 5 5600H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB AMD Radeon RX 6500M Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqpo8t-WtVJKXDKhrhArnrysuhyihDRPwwf54XSRh-hrhhaFhrhrhhacBrWahrhrBi5UttOoi2ohrFB5pkuP7e7XPRd-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1uwBOjec-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 UN.QPFSI.002 Gaming Laptop (AMD Ryzen 5 7535HS/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹64,990",
        "rating": "4.7",
        "specScore": "68",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYVxXvBiaVtI5axhrhAgTYBOr3Uh7rAa3cuYU3scrnic3Iyauc4ctaDrcAs3acG4Z4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcru254cH5cWrnhNcTrBUshDhDh8bHl5a4oog554GhmBYihkwkp7.dG.f1XpK1SvhrhhaFhrhrhhacBrWahrhrBi5osaW8ZgXhrFB53Nz23dp7791o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ies7R26hk-w280-h280/hp-victus-15-fa0888t.webp",
        "productName": "HP Victus 15-FA0888TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹67,999",
        "rating": "4.2",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0H5Q-u0r8EKlYqChrhAA3snrh7tBc2YAUCFc54cYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoPo5cBa3gs3nruAac6TCacocZGcOWch-hDZPbZ45hrhhaFhrhrhhacBrWahrhrBi5QGOailtUhrFB5PHAi__s5CK_A"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAfj0NSRR-w280-h280/msi-crosshair-16-hx.webp",
        "productName": "MSI Crosshair 16 HX D14VGKG-205IN Gaming Laptop (14th Gen Core i7/ 32GB/ 1TB SSD/ Win11 Home/ 8GB RTX4070)",
        "price": "₹1,89,990",
        "rating": "4.5",
        "specScore": "83",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB~~fadqtaGI_HQVhrhArnrysuhyihDRPw0V.lS~dh-hrhhaFhrhrhhacBrWahrhrBi5oZltrlbQhrFB5b~7mFfwt.3EH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itYQv0Unl-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Edge Laptop (Snapdragon X Elite/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,62,990",
        "rating": "4.4",
        "specScore": "51",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25204%2520Edge%2520Laptop%2520(Snapdragon%2520X%2520Elite%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inIfI5z9u-w280-h280/xiaomi-redmi-g-pro-2.webp",
        "productName": "Xiaomi Redmi G Pro 2024 Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ RTX 4060)",
        "price": "₹1,02,990",
        "rating": "4.25",
        "specScore": "78",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520G%2520Pro%25202024%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252016GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%2520RTX%25204060)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRHfT09Qw-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-52 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹32,990",
        "rating": "4.55",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiCNynvVbdD8_iUz.hrhAA3snrh7rAa3crFBY3acThscYuUaTcAs3acYZc5oUtcWaucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55c54cbcYuAtcTaic6huTYUciYFBTrIcFUaaTcW3rIc5c4lcOWch-hDZPZZbGhrhhaFhrhrhhacBrWahrhrBi55AlDoPAFhrFB5OlxHeGaagVI2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2WS1LNEs-w280-h280/zebronics-pro-series.webp",
        "productName": "Zebronics Pro Series Z ZEB-NBC 3S 2023 Laptop (12th Gen Core i3 / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹24,990",
        "rating": "4.4",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqHBxNBYBPK-I~ihrhArnrysuhyihDRPw--Gf.pwh-hrhhaFhrhrhhacBrWahrhrBi5NtN8lit3hrFB5g9Dv7ue-o.z6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUf9FU6F7-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15  FX506HF-HN075W Gaming Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹50,890",
        "rating": "4.4",
        "specScore": "62",
        "features": [
            "11th Gen Intel Core i5 11260H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqVakHE6m6dmasJhrhArnrysuhyihDRPwfw-b7oSh-hrhhaFhrhrhhacBrWahrhrBi584sUgi8IhrFB5BePqiKT55Jzb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idldYIvKz-w280-h280/asus-tuf-gaming-f17.webp",
        "productName": "Asus TUF Gaming F17 FX707ZC4-HX067W Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹73,989",
        "rating": "4.45",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFHjrUqJJi5pyJhrhArnrysuhyihDRPwX--Je_1h-hrhhaFhrhrhhacBrWahrhrBi5WG6UHnsUhrFB5mCYRx8N.pjIk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iH4FwlZ9q-w280-h280/infinix-zerobook-202.webp",
        "productName": "Infinix Zerobook 2023 Laptop (13th Gen Core i9/ 32GB/ 1TB SSD/ Win 11 Home)",
        "price": "₹64,990",
        "rating": "4.05",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOPPR8erfeATxC2hrhAgTYBOr3Uh7YugYuYDcya3s6ssOc5ZcYuUaTcAs3acYlc5ZUtcWauc5ZlPPtcZocW6c5cU6cFFic8Yuis8Fc55ctsnacyT45ZcUtYucTYWtUcTrBUshDhDh84ZXbbaa6o56b4hmBYihkwkp7vx17fwVxe7.7hrhhaFhrhrhhacBrWahrhrBi5Y8guZnPYhrFB5pURq3C1x.smv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itWBJGHfj-w280-h280/asus-vivobook-14x-ol.webp",
        "productName": "Asus Vivobook 14X OLED 2023 K3405VCB-KM542WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/4 GB Graphics)",
        "price": "₹72,990",
        "rating": "4.65",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA Geforce RTX 3050",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOHyqGrWJy4e006hrhAgTYBOr3Uh7rFCFc2Y2s6ssOc5HDcsTaicoPoZcA3arUs3cYuUaTctcFa3YaFcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PclPctyc4PcUWBcOZHP42A6cOn4Ho8FcWrnhNcTrBUshDhDh8iGAZHHXGol6AZhmBYihkwkp7.pVxKzb7RX7ohrhhaFhrhrhhacBrWahrhrBi5aAWBalPthrFB5DH_mFfrXwDAo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUVL4a1Ah-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2023 X1504VA-NJ321WS Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,990",
        "rating": "4.35",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GHgevHZHb0qG77hrhAA3snrh7rFCFc2Y2s6ssOc54cYuUaTcAs3acYZc5oUtcWaucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5cAssTcFYThCc5cGcOWch-hDZPb5lohrhhaFhrhrhhacBrWahrhrBi5QUAsPZUAhrFB5OiBK-yE.Zx6S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iABuyKcMV-w280-h280/msi-modern-14-c7m-06.webp",
        "productName": "MSI Modern 14 C7M-062IN Laptop (Ryzen 5 7530U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹36,990",
        "rating": "4.55",
        "specScore": "59",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzgtIepsxDqzJNWhrhAgTYBOr3Uh7nFYcnsia3uc5Hcrnic3Iyauc4ctaDrcAs3acG4ZPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacAGncPboYucUtYucTYWtUcTrBUshDhDh8Hl5gbAXbggG4AhmBYihkwkp7p0b0dw-Gzzf0hrhhaFhrhrhhacBrWahrhrBi5t4orNa6GhrFB5R5-qfHv6izms"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC1uclsPb-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2022 Laptop (Apple M2/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹89,990",
        "rating": "4.15",
        "specScore": "47",
        "features": [
            "Apple M2",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "8-Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbRSXToDs3r5mu7PDsVxhrhAgTYBOr3Uh7rBBTacoPoocnrA6ssOcrY3cnocXcW6co4bcW6cFFicnrAcsFcnsuhUaIcnTIZZtucrh-hDh8PlHbAP4abZZ4AhmBYihkwkp7xRo7pwv_.7X4hrhhaFhrhrhhacBrWahrhrBi5TaWyNYu2hrFB5Ja_5a9RtgYeA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-immNOIQcO-w280-h280/hp-15-fd0111tu-lapto.webp",
        "productName": "HP 15-fd0111TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹53,999",
        "rating": "4.2",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwWSUwWQuRYKfl1hrhArnrysuhyihDRPKw7GZzdVh-hrhhaFhrhrhhacBrWahrhrBi5u5aIbigrhrFB586TYnX5rEFDC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJrP56MSY-w280-h280/lenovo-loq-15arp9-83.webp",
        "productName": "Lenovo LOQ 15ARP9 83JC0046IN Gaming Laptop (AMD Ryzen 7 7435H/ 24GB/ 512GB SSD/ Win11/ 8GB RTX 4060 Graph)",
        "price": "₹98,990",
        "rating": "4.65",
        "specScore": "72",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "24 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqTFwXZSJAKjqYghrhArnrysuhyihDRPKGX1Rve1h-hrhhaFhrhrhhacBrWahrhrBi5rZ32bYZIhrFB5_rrdtkwGqFTP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLH4fh4Iu-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83EQ005VIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,890",
        "rating": "4.55",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwguJxm9yo~IadyhrhArnrysuhyihDRPKbp10dGRh-hrhhaFhrhrhhacBrWahrhrBi5o3Gb4lbghrFB5BH56Rzyzs07l"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3pwgLTX6-w280-h280/asus-vivobook-16-x16.webp",
        "productName": "Asus Vivobook 16 X1605ZAC-MB740WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.7",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwni4OiTyjEROruhrhArnrysuhyihDRPKX-V4GoSh-hrhhaFhrhrhhacBrWahrhrBi5l5AlZHbQhrFB5gk077WWd0e_a"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iynSkXaUn-w280-h280/hp-15s-eq2305au-lapt.webp",
        "productName": "HP 15s-eq2305AU Laptop (AMD Ryzen 5 5500U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,790",
        "rating": "4.3",
        "specScore": "59",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqqQPqgnUPJjZd6hrhArnrysuhyihDRPwfop-Gmmh-hrhhaFhrhrhhacBrWahrhrBi5U8bYCyiChrFB5diwvIu2xVqfp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iESGeKIYW-w280-h280/hp-15s-fq5330tu-lapt.webp",
        "productName": "HP 15s-fq5330TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,799",
        "rating": "4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67PdkY-5CHu1IiNhrhArnrysuhyihDRPwzVSzdJmh-hrhhaFhrhrhhacBrWahrhrBi54QXTi3sWhrFB5q1OrISNF~mlN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNYAjEPov-w280-h280/ultimus-elite-nu14u3.webp",
        "productName": "Ultimus Elite NU14U3INF56BN-CS Laptop (10th Gen Core i5 / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹19,999",
        "rating": "4.2",
        "specScore": "50",
        "features": [
            "10th Gen Intel Core i5 1035G4",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris",
            "14.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQfsgP00CBCnf4uhrhAgTYBOr3Uh7CTUYnCFcaThscYuUaTcAs3acY4c5PUtcWauc5PZ4WHcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacuC5HCZYug4b6ucn6cUtYucTYWtUcTrBUshDhDh86o544lAAPliXihmBYihkwkp7fHoR_17pKVq-hrhhaFhrhrhhacBrWahrhrBi5U5FI6NrihrFB5U-zyjPQ0~qx3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyOWM2L6n-w280-h280/hp-chromebook-x360-1.webp",
        "productName": "HP Chromebook x360 ‎14a-ca0505TU Laptop (Intel Celeron N4120/ 4GB/ 64GB eMMC/ Chrome OS)",
        "price": "₹17,990",
        "rating": "4.05",
        "specScore": "41",
        "features": [
            "Intel Celeron  N4120",
            "Quad Core, 4 Threads",
            "4 GB DDR4 RAM",
            "64 GB Hard Disk",
            "Intel Integrated UHD 600",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzEdArUXErRxnXnhrhAgTYBOr3Uh7tBcAt3sna6ssOcYuUaTcAaTa3suciCrTcAs3acuHPoPcHcW6cbHcW6cannAcFUs3rWacAt3snacsFc5HrcArP4P4UCcTrBUshDhDh8XlXH6Z5lXo6PrhmBYihkwkp7RSVxfZzZS.R1hrhhaFhrhrhhacBrWahrhrBi5yPXlQ6CQhrFB5BJy0FOguKCpB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipu08KXpr-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 2022 FX507ZC4-HN116W Gaming Laptop (12th Gen Core i5/ 16GB/512GB SSD/ Win11 / 4GB Graph)",
        "price": "₹73,990",
        "rating": "4.45",
        "specScore": "71",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67KrVOT6oYBHN8phrhArnrysuhyihDRPKHob71JGh-hrhhaFhrhrhhacBrWahrhrBi5IWQ2U46YhrFB5j.TqKxVvNd_6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7KmiNI47-w280-h280/dell-vostro-3481-lap.webp",
        "productName": "Dell Vostro 3481 Laptop (8th Gen Core i5/ 8GB/ 1TB/ Linux/ 2GB Graph)",
        "price": "₹46,790",
        "rating": "4.65",
        "specScore": "54",
        "features": [
            "8th Gen Intel Core i5 8265U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "2 GB AMD Radeon 520",
            "14 inches, 1366 x 768 pixels",
            "Linux OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYl9fvgg7tIPVorhrhAgTYBOr3Uh7iaTTc2sFU3sc5HcZPPPcYuUaTcAs3acY4cXUtcWaucXob4CcXcW6c5cU6ctiicTYuCDcocW6cW3rBtYAFc2sFcZHXPcTrBUshDhDh8ZbrlPb5gAlG6rhmBYihkwkpxSzSv17ejlK..hrhhaFhrhrhhacBrWahrhrBi5FCtulBoZhrFB5nKnU-V6mo6Qy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iv0oRgUsR-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹29,990",
        "rating": "4.1",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtI8Yq4T2CQmTOyhrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8GH4oZHGgroHoXhmBYihkwkpSfoHv-Sof_017hrhhaFhrhrhhacBrWahrhrBi52BXQQYFQhrFB5PbK13df7O1lF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieIs3BTFq-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX507VV-LP287W Gaming Laptop (13th Gen Core i7/ 16GB/512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,09,990",
        "rating": "4.05",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sggvmknD7qirq9VChrhAA3snrh7rFCFcUCgcYuUaTcAs3acYGc5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55cXW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcHPbPcW3rBthschncococOWch-hDZPbZ4PhrhhaFhrhrhhacBrWahrhrBi5yBFQsTYThrFB5-4zl.nWHJAEP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iejYjCfVr-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00BHIN Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050)",
        "price": "₹76,490",
        "rating": "4.05",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFiiljP7punTylJhrhAgTYBOr3Uh7Taus2scTsNcoPoHcYuUaTcAs3acY4c5ZUtcWauc5ZH4PtDc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54Y3DliocWrnhNcTrBUshDhDh84oaHoaPZPHoAbhmBYihkwkp7fex7S1eJ7.e0hrhhaFhrhrhhacBrWahrhrBi5rgbPoDOZhrFB5U~X1FVKnKUWg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikfAgTiMr-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS008VIN Gaming Laptop (12th Gen Core i5/ 12GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,490",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "12 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ8wiVEagaQ0w7BhrhAgTYBOr3Uh7Taus2scTsNcoPoHcYuUaTcAs3acY4c5oUtcWauc5oH4PtDc5ocW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54YrDli5cWrnhNcTrBUshDhDh8bo4b6gXAHroG4hmBYihkwkpSfl.Xjx01S0-xhrhhaFhrhrhhacBrWahrhrBi5B588HIr4hrFB5EgGHVBei9A5j"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLBYLoFaT-w280-h280/chuwi-corebook-x-lap.webp",
        "productName": "Chuwi CoreBook X Laptop (10th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹24,990",
        "rating": "4.7",
        "specScore": "51",
        "features": [
            "10th Gen Intel Core i5 1035G1",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 2160 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqHBxNBYBPK-I~ihrhArnrysuhyihDRPwdzbmKbJh-hrhhaFhrhrhhacBrWahrhrBi5b4ayssTQhrFB5U8n1XCkFwF.C"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHYJzC0np-w280-h280/zebronics-zeb-nbc-5s.webp",
        "productName": "Zebronics ZEB-NBC 5S Laptop (12th Gen Core i7 / 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹37,990",
        "rating": "4.05",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqwHTwaDlkUZIfUhrhArnrysuhyihDRPw-Gov.zRh-hrhhaFhrhrhhacBrWahrhrBi5BITrPXaOhrFB5HKyTv-Yzebo3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iISv847hY-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2024 Laptop (Apple M3/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹1,04,990",
        "rating": "4.25",
        "specScore": "46",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "8 GB  RAM",
            "256 GB SSD",
            "Apple 8 Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFw~uJvR.aREujtvjXhrhAgTYBOr3Uh7rBBTacnrA6ssOcrY3cnZcXcW6co4bcW6cFFicnrAsFcFsusnrcn3DNZtucrh-hDh8rir5AAZGalA6HhmBYihkwkp7f1477.dGSeZ.hrhhaFhrhrhhacBrWahrhrBi55NG3WlZHhrFB5ZK6uZTwgjq_Y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikiww9ae6-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2023 K3605ZU-MB541WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹79,990",
        "rating": "4.3",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA Geforce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI_5baB~z1VRleihrhArnrysuhyihDRPw4dHVlSRh-hrhhaFhrhrhhacBrWahrhrBi5YbnQyY5UhrFB5fu0Q~A41zHxZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icLedCxeu-w280-h280/hp-15s-fq5007tu-lapt.webp",
        "productName": "HP 15s-fq5007TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.65",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G4Gf7uFVF_B3TnhrhAA3snrh7tBc54FcgN4ZoGUCcYuUaTcAs3acYZc5oUtcWaucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5cblcOWch-hDobX5PHhrhhaFhrhrhhacBrWahrhrBi58XIYYlOUhrFB54vP2PQCgPy4i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imJYwG93q-w280-h280/dell-inspiron-3520-d.webp",
        "productName": "Dell Inspiron 3520 D560896WIN9B Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,750",
        "rating": "4.75",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JU2P8VSQS1avoIAhrhAgTYBOr3Uh7iaTTcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacua8cYuFBY3suc54cTrBUsBcUtYucTYWtUh-hDh8PbarbGHrZ6i46hmBYihkwkp7-G4Swwx-eXjqhrhhaFhrhrhhacBrWahrhrBi5TbI4lrOUhrFB5ZtSefquE1NnF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQ2AwqUqH-w280-h280/hp-pavilion-15-eg200.webp",
        "productName": "HP Pavilion 15-eg2009TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹58,790",
        "rating": "4.25",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xEf6QJ6fUFPp3ShrhAgTYBOr3Uh7tBcBr2YTh3coPoHcYuUaTcAs3acY4c5oUtcWauc5oHPBcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54caWoPPlUCcUtYucTYWtUcTrBUshDhDh8lXil65Zi44ZoghmBYihkwkp7wvf77p.xde1.hrhhaFhrhrhhacBrWahrhrBi5nXQGlnZQhrFB5QPKVKqSitgV9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEFytCIeV-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2024 MXCV3HN/A Laptop (Apple M3/ 16GB/ 256GB SSD/ MacOS)",
        "price": "₹1,34,900",
        "rating": "4.05",
        "specScore": "50",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "16 GB  RAM",
            "256 GB SSD",
            "Apple 10 Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG0RfYJrw6sNytGBhrhAgTYBOr3Uh7rBBTacnrA6ssOcrY3cnZc5bcW6co4bcW6cFFicnrAsFcFsusnrcnDA2Ztucrh-hDh8alPgaZlG5laPahmBYihkwkpSoe.xGSS-xxE-hrhhaFhrhrhhacBrWahrhrBi5tFHXnaNahrFB5.tZsZBXux-gn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizWzm3cu-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-79G UN.34PSI.001 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹64,990",
        "rating": "4.7",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYVxXvBiaVtI5axhrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcrG54cGlWcWrnhNcTrBUshDhDh8Hgilgb4oloHPZhmBYihkwkpSZ7lbpf7Je7zxhrhhaFhrhrhhacBrWahrhrBi5i3UB226UhrFB51JlNV5yE0zJK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTx4gJVxW-w280-h280/asus-tianxuan-air-20.webp",
        "productName": "Asus Tianxuan Air 2024 Gaming Laptop (Ryzen AI 9 HX 370/ 32GB/ 1TB SSD/ 6GB RTX 4060)",
        "price": "₹1,09,670",
        "rating": "4.25",
        "specScore": "47",
        "features": [
            "AMD Ryzen AI 9",
            "32 GB  RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520Tianxuan%2520Air%25202024%2520Gaming%2520Laptop%2520(Ryzen%2520AI%25209%2520HX%2520370%252F%252032GB%252F%25201TB%2520SSD%252F%25206GB%2520RTX%25204060)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNi7Ud2yk-w280-h280/hp-15-fd0316tu-lapto.webp",
        "productName": "HP 15-fd0316TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹55,990",
        "rating": "4",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "‎Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwtRDQTNQFF4z-YhrhArnrysuhyihDRPKHmJfJxlh-hrhhaFhrhrhhacBrWahrhrBi5PCQTZIZQhrFB5_YBfOJV-vCUu"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipmRyoxwu-w280-h280/dell-16-inspiron-563.webp",
        "productName": "Dell 16 Inspiron 5630 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹91,821",
        "rating": "4.05",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqYaK8YPQye41PEhrhArnrysuhyihDRPw_5zHSVwh-hrhhaFhrhrhhacBrWahrhrBi5AiAtOACthrFB5rCurjWUUbi4u"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9VL7hdct-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ745WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹61,990",
        "rating": "4.35",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwT7sx~9j3xf36dhrhArnrysuhyihDRPKZm~vSJwh-hrhhaFhrhrhhacBrWahrhrBi5yOu4a8WbhrFB51_qeQUbKZnZT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAB4DNuA9-w280-h280/hp-pavilion-plus-14.webp",
        "productName": "HP Pavilion Plus 14-ew1082TU Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹83,990",
        "rating": "4.6",
        "specScore": "62",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "14 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqiY0bOkagewdSkhrhArnrysuhyihDRPKHz_.J4vh-hrhhaFhrhrhhacBrWahrhrBi5WoTn462nhrFB5C1V2uZsOTYTD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBuCckD9W-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00LXIN Gaming Laptop (13th Gen Core i7/ 24GB/ 512GB SSD/ Win11/ 8GB RTX4060)",
        "price": "₹1,10,490",
        "rating": "4.4",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "24 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB7UKNn6fonDte4vhrhArnrysuhyihDRPKZz7dfl7h-hrhhaFhrhrhhacBrWahrhrBi5aDtCol2QhrFB5WE0PysjP6z48"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ippGWPj0E-w280-h280/asus-proart-p16-2024.webp",
        "productName": "Asus ProArt P16 2024 Laptop (AMD Ryzen AI 9 HX 370/ 32GB/1TB SSD/ 8GB RTX 4070 Graphics)",
        "price": "₹1,99,990",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "AMD Ryzen AI 9 HX 370",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520ProArt%2520P16%25202024%2520Laptop%2520(AMD%2520Ryzen%2520AI%25209%2520HX%2520370%252F%252032GB%252F1TB%2520SSD%252F%25208GB%2520RTX%25204070%2520Graphics)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieB4kukke-w280-h280/asus-tuf-gaming-a14.webp",
        "productName": "Asus TUF Gaming A14 2024 Gaming Laptop (AMD Ryzen 9 AI HX 370/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,77,990",
        "rating": "4.4",
        "specScore": "61",
        "features": [
            "AMD Ryzen 9 AI HX 370",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520TUF%2520Gaming%2520A14%25202024%2520Gaming%2520Laptop%2520(AMD%2520Ryzen%25209%2520AI%2520HX%2520370%252F%252016GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4isbjKFq-w280-h280/lenovo-yoga-slim-7x.webp",
        "productName": "Lenovo Yoga Slim 7x Laptop (Snapdragon X Elite/ 16GB/ 1TB SSD/ Windows 11 Home)",
        "price": "₹1,39,990",
        "rating": "4.25",
        "specScore": "53",
        "features": [
            "Qualcomm Snapdragon X Elite X1E78100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "14.5 inches, 2944 x 1840 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DLenovo%2520Yoga%2520Slim%25207x%2520Laptop%2520(Snapdragon%2520X%2520Elite%252F%252016GB%252F%25201TB%2520SSD%252F%2520Windows%252011%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMOXQa3Mw-w280-h280/hp-victus-15-fa1319t.webp",
        "productName": "HP Victus 15-fa1319TX Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX 4050)",
        "price": "₹80,990",
        "rating": "4.55",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw86jbUD8K1rxnlhrhArnrysuhyihDRPK5f-vo.fh-hrhhaFhrhrhhacBrWahrhrBi5iA62GiIAhrFB5WpbvOu5VSxgV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-if37z16Ww-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS003UIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹70,490",
        "rating": "4.35",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIeTeKGg-NSJHXXhrhArnrysuhyihDRPw_X_1VJ-h-hrhhaFhrhrhhacBrWahrhrBi5Q5Z43ogahrFB5-og_U_uYwvoC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipPNIsNt2-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 np750xgj-kg2in Laptop (13th Gen Intel Core i5-1335U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹62,990",
        "rating": "4.05",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a.-5QzVD9nFRwuW8ThrhArnrysuhyihDRPK5HZe-lvh-hrhhaFhrhrhhacBrWahrhrBi5FT6niaXHhrFB5w6ftkbiZDyvq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipPNIsNt2-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGJ-KG1IN Laptop (Intel Core i5 1335U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹62,990",
        "rating": "4",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb5Dq1OfyW7ZYsnFsbnhrhAgTYBOr3Uh7FrnFCuWcWrTrDIc6ssOHcYuUaTcAs3acY4c5ZUtcWauc5ZZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacuBG4PDWQcOW5YucuBG4PDWQcTW5YucUtYucTYWtUcTrBUshDhDh8XPgb6baAagGXPhmBYihkwkp7.EfKx._SJfJ.hrhhaFhrhrhhacBrWahrhrBi5CaNi6TU2hrFB5zJw0o5BFxFnp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikHXHHUMd-w280-h280/hp-chromebook-11mk-g.webp",
        "productName": "HP Chromebook 11MK G9 EE Laptop (MediaTek MT8183/ 4GB/ 32GB eMMC/ Chrome OS)",
        "price": "₹10,990",
        "rating": "4.75",
        "specScore": "28",
        "features": [
            "MediaTek Kompanio 500 500",
            "Octa Core",
            "4 GB LPDDR4X RAM",
            "32 GB Hard Disk",
            "Arm Mali-G72 MP3",
            "11.6 inches, 1366 x 768 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQEQtpeJFyYOEN-hrhAgTYBOr3Uh7tBcAt3sna6ssOcoPoHcnaiYrUaOcnUX5XZcHcW6cZocW6cannAcFUs3rWacAt3snacsFc55nOcWlcaacTrBUshDhDh86AgA6APr6HoHghmBYihkwkp7.xx__Sd0w4j4hrhhaFhrhrhhacBrWahrhrBi545aAbIgrhrFB5TF1EpWHFan9i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3uUcQ9JG-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2023 K3605ZC-MBN544WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB RTX3050)",
        "price": "₹64,990",
        "rating": "4.1",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqeklx7YU9kIA.EhrhArnrysuhyihDRPw.Zp-VHGh-hrhhaFhrhrhhacBrWahrhrBi5G6nAUICPhrFB5P2GVEQap8pZX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPhbwo8yd-w280-h280/hp-15-fd1099tu-lapto.webp",
        "productName": "HP 15-fd1099TU Laptop (Intel Core Ultra 5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹69,990",
        "rating": "4.65",
        "specScore": "56",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gkl0-N6t~-1dGehrhAA3snrh7tBcgi5PllUCcYuUaTcAs3acCTU3rc4cUtYuchYcTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5c4lcOWch-hDZP4lGHhrhhaFhrhrhhacBrWahrhrBi5PbZQ23ZChrFB5SZXJ7RA8SEsB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZhzuj2rc-w280-h280/asus-vivobook-go-14.webp",
        "productName": "Asus Vivobook Go 14 2023 E1404FA-NK331W Laptop (Ryzen 3 7320U / 8GB/ 1TB SSD/ Win11 Home)",
        "price": "₹33,850",
        "rating": "4.4",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "1 TB SSD",
            "Integrated AMD Radeon Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqjKfa~fC_t7zHmhrhArnrysuhyihDRPw_5JV1Hxh-hrhhaFhrhrhhacBrWahrhrBi5lPUO5ibGhrFB5UbslEq9F7Zv9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2ZY1egVH-w280-h280/msi-thin-a15-ai-b7ve.webp",
        "productName": "MSI Thin A15 AI B7VE-065IN Gaming Laptop (AMD Ryzen 7 7735H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹84,990",
        "rating": "4.25",
        "specScore": "73",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqajr8EK2ekPNA5hrhArnrysuhyihDRPw04K_5_fh-hrhhaFhrhrhhacBrWahrhrBi5syI523CuhrFB59NCRN6txfJjD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iItJKshN3-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Max/ 48GB/ 1TB SSD/ macOS)",
        "price": "₹3,79,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "Apple M3 Max",
            "16 Cores (12P + 4E)",
            "48 GB  RAM",
            "1 TB SSD",
            "40 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NEX9OqoXTT3l3CihrhArnrysuhyihDRPwp4e.Gw1h-hrhhaFhrhrhhacBrWahrhrBi5tuiZOHunhrFB5JI5tpePT.H1R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2FQuQrlD-w280-h280/asus-vivobook-pro-15.webp",
        "productName": "Asus Vivobook Pro 15 M6500QC-HN742WS Laptop (Ryzen 7 5800H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹66,990",
        "rating": "4.1",
        "specScore": "68",
        "features": [
            "5th Gen AMD Ryzen 7 5800H",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzDdaPwZsjFKngshrhAgTYBOr3Uh7rFCFc2Y2s6ssOcB3sc54cA3arUs3crnic3IyaucGcsAUrcAs3ac4XPPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5HHctyc4PcUWBcnb4PPNActuGH58FcWrnhNcTrBUshDhDh85iooPZbZlZX6ghmBYihkwkp7dvdEleq1qp~0hrhhaFhrhrhhacBrWahrhrBi5HXFt2sHihrFB56JkwKnDoQuP2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ih59Pv4z0-w280-h280/hp-pavilion-x360-14.webp",
        "productName": "HP Pavilion x360 14-ek1010TU Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹73,990",
        "rating": "4.15",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PjZ6l51OFy-FWKhrhArnrysuhyihDRPRvzR0eSeh-hrhhaFhrhrhhacBrWahrhrBi5oTtTaPB6hrFB5FaGx06wWi_l4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icLedCxeu-w280-h280/hp-15s-fq5007tu-lapt.webp",
        "productName": "HP 15s-fq5007TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.65",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G4Gf7uFVF_B3TnhrhAA3snrh7tBc54FcgN4ZoGUCcYuUaTcAs3acYZc5oUtcWaucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5cblcOWch-hDobX5PHhrhhaFhrhrhhacBrWahrhrBi58XIYYlOUhrFB54vP2PQCgPy4i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imJYwG93q-w280-h280/dell-inspiron-3520-d.webp",
        "productName": "Dell Inspiron 3520 D560896WIN9B Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,619",
        "rating": "4.75",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xNu2OvfNBHkXymhrhArnrysuhyihDRPRSHv~HJ0h-hrhhaFhrhrhhacBrWahrhrBi5TbI4lrOUhrFB5V8CAgpqwUVpd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIeWViqm0-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HC-HN362WS Gaming Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,890",
        "rating": "4.35",
        "specScore": "66",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90f.6jKWHoZa9OXhrhAgTYBOr3Uh7rFCFcUCgcWrnhNcg54clP8t3c6rUhUIcYuUaTcAs3acY4c55UtcWauc55HPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5HHctycG4cUWBcgD4PbtActuZbo8cTrBUshDhDh8a5PllA4aPAP5HhmBYihkwkp71~q_Vdebdo.phrhhaFhrhrhhacBrWahrhrBi5lXNNHAB3hrFB5-Q1v3SX2.QgS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihPHrf26o-w280-h280/asus-vivobook-s14-ol.webp",
        "productName": "Asus Vivobook S14 OLED S3402ZA-KM501WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.35",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF_P_.IR5nY5ubOhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcF5HcsTaicYuUaTca2sctcFa3YaFcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFZHPoyrcOn4P58FcUtYucTYWtUcTrBUshDhDh8bZ4a6bigb5i5AhmBYihkwkp7w7o7_Ejjpf-xhrhhaFhrhrhhacBrWahrhrBi5FTAB4UWlhrFB5rCmdGtaqDbQK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihkVyuxbZ-w280-h280/dell-precision-5550.webp",
        "productName": "Dell Precision 5550 Laptop (10th Gen Core i7/ 16GB/ 512GB SSD/ Win10 Pro/ 4GB Graph)",
        "price": "₹1,84,999",
        "rating": "4.2",
        "specScore": "66",
        "features": [
            "10th Gen Intel Core i7 10750H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4  RAM",
            "512 GB SSD",
            "4 GB NVIDIA",
            "15.6 inches, 1920 x 1200 pixels",
            "Windows 10 OS",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DDell%2520Precision%25205550%2520Laptop%2520(10th%2520Gen%2520Core%2520i7%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win10%2520Pro%252F%25204GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJryvksNb-w280-h280/msi-titan-18-hx-a14v.webp",
        "productName": "MSI Titan 18 HX A14VIG-201IN Gaming Laptop (14th Gen Core i9/ 128GB/ 4TB SSD/ Win11 Home/ 16GB Graphics RTX 4090)",
        "price": "₹5,49,990",
        "rating": "4.4",
        "specScore": "93",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "128 GB DDR5 RAM",
            "192 GB Hard Disk",
            "4 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREv_r0-nfm8J9gUASthrhArnrysuhyihDRPwzz-VG-Rh-hrhhaFhrhrhhacBrWahrhrBi5CGN3IOBPhrFB5a23S9vYd94fE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTx4gJVxW-w280-h280/asus-tianxuan-air-20.webp",
        "productName": "Asus Tianxuan Air 2024 Gaming Laptop (Ryzen AI 9 HX 370/ 32GB/ 1TB SSD/ 6GB RTX 4060)",
        "price": "₹1,09,670",
        "rating": "4.25",
        "specScore": "47",
        "features": [
            "AMD Ryzen AI 9",
            "32 GB  RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520Tianxuan%2520Air%25202024%2520Gaming%2520Laptop%2520(Ryzen%2520AI%25209%2520HX%2520370%252F%252032GB%252F%25201TB%2520SSD%252F%25206GB%2520RTX%25204060)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNZsloWbR-w280-h280/acer-aspire-3-14-a32.webp",
        "productName": "Acer Aspire 3 14 A324-45 Laptop (Intel Core Celeron N4500/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹19,990",
        "rating": "4.25",
        "specScore": "39",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtUZEdE51NRv5lShrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacrZoHcH4cUtYucTYWtUcTrBUshDhDh8P4XrbPZGGZbP6hmBYihkwkpSx.f.Sj4f-SeZhrhhaFhrhrhhacBrWahrhrBi5tX6PDQYnhrFB5_8lpPvZGlvBB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQiKawVuP-w280-h280/infinix-zero-book-ul.webp",
        "productName": "Infinix Zero Book Ultra AI PC ZL514 Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win 11 Home)",
        "price": "₹84,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Intel Arc",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYJ5rlZXWzuuJ3ghrhAgTYBOr3Uh7YugYuYDcya3sc6ssOcCTU3rcrYcBAcYuUaTcAs3aclc5X4tcZocW6c5cU6cFFic8Yuis8Fc55ctsnacyT45HcUtYucTYWtUcTrBUshDhDh8GXirrHPrbPbZZhmBYihkwkpSxf.dd4_RdxKJhrhhaFhrhrhhacBrWahrhrBi5HITAN6sAhrFB59x01TjND.l6N"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipmRyoxwu-w280-h280/dell-16-inspiron-563.webp",
        "productName": "Dell 16 Inspiron 5630 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹91,799",
        "rating": "4.05",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqYiVvNCm5bU0-JhrhArnrysuhyihDRPw_5zHSVwh-hrhhaFhrhrhhacBrWahrhrBi5AiAtOACthrFB5rCurjWUUbi4u"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifHKwQY9N-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-71 NX.KF1SI.007 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹71,990",
        "rating": "4",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYknHuKCp4XZJQ1hrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcsTaicoPoHca2scYuUaTcAs3acYGc5ZUtcWauc5ZGPPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacFgW5HcG5cGP6WcUtYucTYWtUcTrBUshDhDh8rZibl666rAXHAhmBYihkwkpSxzxfp~JGJfJqhrhhaFhrhrhhacBrWahrhrBi5nNlioaBghrFB5iGS6FsWWbJxH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifHKwQY9N-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-71 NX.KF1SI.006 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.25",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYVxXvBiaVtI5axhrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcsTaicoPoHca2scYuUaTcAs3acYGc5ZUtcWauc5ZGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFgW5HcG5cUtYucTYWtUcTrBUshDhDh8bgAbAXrXlbZZlhmBYihkwkpSxzf.X4vqpG7KhrhhaFhrhrhhacBrWahrhrBi5Q5YtOOyuhrFB55m.9jaTmP5Rr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irAri6DAM-w280-h280/lenovo-loq-15arp9-83.webp",
        "productName": "Lenovo LOQ 15ARP9 83JC0078IN Gaming Laptop (AMD Ryzen 5 7235HS/ 24GB/ 512GB SSD/ Win11/ 6GB RTX 3050 Graph)",
        "price": "₹73,990",
        "rating": "4",
        "specScore": "65",
        "features": [
            "7th Gen AMD Ryzen 5 7235HS",
            "Quad Core, 8 Threads",
            "24 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY1W7etfUiKS5OvhrhAgTYBOr3Uh7Taus2scTsNcoPoHcrnic3Iyauc4cNCricAs3acGoZ4tFcoHcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54r3BlcWrnhNcTrBUshDhDh8iZg66iAaioib6hmBYihkwkpSxf.ZxK0d0-EGhrhhaFhrhrhhacBrWahrhrBi5XyZuGttIhrFB5Jps2Adv2PIH_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7nDRfKv9-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QKIN Laptop (AMD Ryzen 5 7535HS / 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹64,990",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqeklx7YU-9Rmk6hrhArnrysuhyihDRPKXSJ5Z_1h-hrhhaFhrhrhhacBrWahrhrBi5guANHXCQhrFB5vD.BVizA~dP9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4IYOUCuE-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00LWIN Gaming Laptop (13th Gen Core i5/ 24GB/ 512GB SSD/ Win11/ 6GB RTX4050)",
        "price": "₹85,490",
        "rating": "4.25",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "24 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0Hw~aOurG6NBpREhrhAA3snrh7Taus2scTsNc54Y3DlcYuUaTcAs3acY4c5ZUtcWaucWrnhNcTrBUsBcoHW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcHP4PcnFcsggYAacoPo5cTCurcW3aIcocZXcOWch-hDZPGHZlhrhhaFhrhrhhacBrWahrhrBi5rNUFAyIYhrFB5ZpNieTwPi5bV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOOUU9J8E-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 15IRH8 83EM009YIN Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹67,290",
        "rating": "4.25",
        "specScore": "56",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYmp9o.g3PaNupvhrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcAs3acYGc5ZUtcWaucAs3acYGc5ZboPtc5PAcbBcHac5bUcBcAs3acocHcHclWtycacAs3ac5cXcZcbWtyc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54Y3tXcUtYucTYWtUcTrBUshDhDh8AbrPg6AHaZ6aahmBYihkwkpSoGz.Vl1v7.f.hrhhaFhrhrhhacBrWahrhrBi54ZyQWTyFhrFB5N5yqWpymOaIS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9VL7hdct-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ745WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹61,990",
        "rating": "4.35",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwT7sx~9j3xf36dhrhArnrysuhyihDRPKZm~vSJwh-hrhhaFhrhrhhacBrWahrhrBi5yOu4a8WbhrFB51_qeQUbKZnZT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iymb9nXEH-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 (Snapdragon X Elite/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,50,990",
        "rating": "4.5",
        "specScore": "51",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "16 GB ‎LPDDR5x RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.8 inches, 2304 x 1536 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uDyXyrRXVEwXX.bUhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5ZcXcYuAtcYBFciYFBTrIcBTrUYuCnc5cZHcOWch-hDZPX45ZhrhhaFhrhrhhacBrWahrhrBi5XlWQ4CUPhrFB57WCq8x49qePq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqLqVUZLP-w280-h280/hp-victus-15-fa1279t.webp",
        "productName": "HP Victus 15-FA1279TX Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX4050)",
        "price": "₹78,999",
        "rating": "4",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HXHiz3jQVuWKpXhrhAA3snrh7tBc2YAUCFc54cYuUaTcAs3acY4c5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55cbW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcHP4PcnFcsggYAacoPo5cnYArcFYThCcocXGcOWch-hDZPbHPXhrhhaFhrhrhhacBrWahrhrBi556lUZCWHhrFB51o3PUEm-bDIC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuW0r673n-w280-h280/msi-thin-15-b12ucx-1.webp",
        "productName": "MSI Thin 15 B12UCX-1694IN Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX 2050 Graph)",
        "price": "₹62,849",
        "rating": "4.35",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqvv4RUJEo228IzhrhArnrysuhyihDRPw0leG.0bh-hrhhaFhrhrhhacBrWahrhrBi5rUrDQPZDhrFB5t006ReU_Os1X"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3eJoUNH7-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-58GM Gaming Laptop ( Intel Core i5 13420H / 16GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹56,990",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwtaZ.0WPaCtKBqhrhArnrysuhyihDRPK57GRbbmh-hrhhaFhrhrhhacBrWahrhrBi5yYFB6gAihrFB53WCK3sl2sWJ_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-if37z16Ww-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS003UIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹70,490",
        "rating": "4.35",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqJ9Rs3N6WGSokShrhArnrysuhyihDRPw_X_1VJ-h-hrhhaFhrhrhhacBrWahrhrBi5Q5Z43ogahrFB5-og_U_uYwvoC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipPNIsNt2-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGJ-KG1IN Laptop (Intel Core i5 1335U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹62,990",
        "rating": "4",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb5Dq1OfyW7ZYsnFsbnhrhAgTYBOr3Uh7FrnFCuWcWrTrDIc6ssOHcYuUaTcAs3acY4c5ZUtcWauc5ZZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacuBG4PDWQcOW5YucuBG4PDWQcTW5YucUtYucTYWtUcTrBUshDhDh8XPgb6baAagGXPhmBYihkwkp7.EfKx._SJfJ.hrhhaFhrhrhhacBrWahrhrBi5CaNi6TU2hrFB5zJw0o5BFxFnp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipPNIsNt2-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGJ-KG3IN Laptop (Intel Core i7 1355U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹72,990",
        "rating": "4.6",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a.-SFU91aYWHt7Wy0hrhArnrysuhyihDRPK5Z.GmRxh-hrhhaFhrhrhhacBrWahrhrBi5CaFDDHCUhrFB5G9uRkq7sAaUn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikHXHHUMd-w280-h280/hp-chromebook-11mk-g.webp",
        "productName": "HP Chromebook 11MK G9 EE Laptop (MediaTek MT8183/ 4GB/ 32GB eMMC/ Chrome OS)",
        "price": "₹10,990",
        "rating": "4.75",
        "specScore": "28",
        "features": [
            "MediaTek Kompanio 500 500",
            "Octa Core",
            "4 GB LPDDR4X RAM",
            "32 GB Hard Disk",
            "Arm Mali-G72 MP3",
            "11.6 inches, 1366 x 768 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzvwDOYm6lFyJrjhrhAgTYBOr3Uh7tBcAt3sna6ssOcoPoHcnaiYrUaOcnUX5XZcHcW6cZocW6cannAcFUs3rWacAt3snacsFc55nOcWlcaacTrBUshDhDh86AgA6APr6HoHghmBYihkwkp7.xx__Sd0w4j4hrhhaFhrhrhhacBrWahrhrBi545aAbIgrhrFB5TF1EpWHFan9i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPhbwo8yd-w280-h280/hp-15-fd1099tu-lapto.webp",
        "productName": "HP 15-fd1099TU Laptop (Intel Core Ultra 5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹69,990",
        "rating": "4.65",
        "specScore": "56",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3VATYb~1rzak3-hrhAA3snrh7tBcgi5PllUCcYuUaTcAs3acCTU3rc4cUtYuchYcTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5c4lcOWch-hDZP4lGHhrhhaFhrhrhhacBrWahrhrBi5PbZQ23ZChrFB5SZXJ7RA8SEsB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iiT0w46tE-w280-h280/infinix-inbook-y3-ma.webp",
        "productName": "Infinix INBook Y3 Max Series YL613 Laptop (12th Gen Core i3/ 16GB/ 256GB SSD/ Win 11)",
        "price": "₹36,990",
        "rating": "4.4",
        "specScore": "48",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFvDWvulg5dueP9IhrhAgTYBOr3Uh7YugYuYDcIZcnrDcFa3YaFcYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6co4bcW6cFFic8Yuis8Fc55cB3scITb5ZcUtYucTYWtUcTrBUshDhDh8oG45ZA5Z45AX4hmBYihkwkpSZHEZo_~SVvd7hrhhaFhrhrhhacBrWahrhrBi53IIFTCnihrFB5j3V4izYXxJ42"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSX7KGO7P-w280-h280/msi-thin-a15-ai-b7vf.webp",
        "productName": "MSI Thin A15 AI B7VF-064IN Gaming Laptop (AMD Ryzen 7 7735H/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹99,990",
        "rating": "4.35",
        "specScore": "75",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqnVSDubukxTyqRhrhArnrysuhyihDRPw04K4dJeh-hrhhaFhrhrhhacBrWahrhrBi5OuDPanNNhrFB5PoS7zAUInKWU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inQ5Ps4SE-w280-h280/hp-omen-16-wf0179tx.webp",
        "productName": "HP Omen 16-wf0179TX Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹99,990",
        "rating": "4",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16.1 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqnVSDubu1XImT-hrhArnrysuhyihDRPwzpw.4mHh-hrhhaFhrhrhhacBrWahrhrBi52ClCGHQshrFB5lCGQxNouYDGr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNWUMOLr9-w280-h280/hp-15-fd0221tu-lapto.webp",
        "productName": "HP 15-fd0221TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹55,990",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67oYHQ5OfGseNQIhrhArnrysuhyihDRPwzVS7Zxbh-hrhhaFhrhrhhacBrWahrhrBi5bgn2lWaahrFB5s3N8pU79Ravu"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJUFU814v-w280-h280/honor-magicbook-x16.webp",
        "productName": "Honor MagicBook X16 2024 ‎Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹49,717",
        "rating": "4.1",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwi5fmafq94wEuwhrhArnrysuhyihDRPwv~RHSR1h-hrhhaFhrhrhhacBrWahrhrBi5iBgPNIO3hrFB5GAyCz-VpYVlr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ite39wTdj-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-52 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹42,990",
        "rating": "4.4",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbRSXTo_4-m1fB__ofVuhrhAgTYBOr3Uh7rAa3cYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh8HHGgXbGHaal44hmBYihkwkpSoXEHXjd-xGS.hrhhaFhrhrhhacBrWahrhrBi5AOg3Z8PZhrFB5F.F4mQFFZWTb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iItJKshN3-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Max/ 48GB/ 1TB SSD/ macOS)",
        "price": "₹3,79,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "Apple M3 Max",
            "16 Cores (12P + 4E)",
            "48 GB  RAM",
            "1 TB SSD",
            "40 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NEX9OqoXTT3l3CihrhArnrysuhyihDRPwp4e.Gw1h-hrhhaFhrhrhhacBrWahrhrBi5tuiZOHunhrFB5JI5tpePT.H1R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iceYatBu6-w280-h280/hp-15s-fr5012tu-lapt.webp",
        "productName": "HP 15s-FR5012TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹37,990",
        "rating": "4.65",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZOZ_GSuukO3lQ8hrhAA3snrh7tBc54Fcg34P5oUCcYuUaTcAs3acYZc5oUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5cYuUaTcCticgCTTcticiYFBTrIcurUC3rTcFYThCcl584ZBrch-hDZPoHZGhrhhaFhrhrhhacBrWahrhrBi5tbn32GWDhrFB5JOGC_iyTeyNa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuf6vBFtp-w280-h280/hp-victus-16-s0095ax.webp",
        "productName": "HP Victus 16-s0095AX Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹78,990",
        "rating": "4",
        "specScore": "72",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFaYXT_qAD~d_OJhrhAgTYBOr3Uh7tBc2YAUCFcrYcBs8ahBcrnic3IyaucGcsAUrcAs3acGXHPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5bcFPPl4rDcWrnhNcTrBUshDhDh8bHraliiAoiaAbhmBYihkwkp7eo_.7.Sq-q.7hrhhaFhrhrhhacBrWahrhrBi5yinIHYH5hrFB5aTxa4dfERgry"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKqCat16t-w280-h280/hp-omen-16-xf0060ax.webp",
        "productName": "HP Omen 16-xf0060AX Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,13,990",
        "rating": "4.7",
        "specScore": "78",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJEPGnF2ueOVyw~HhrhArnrysuhyihDRPww0.1XZ4h-hrhhaFhrhrhhacBrWahrhrBi5ZnNWF8HHhrFB5swKCZpnX7e6e"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEFIDtnnC-w280-h280/hp-victus-16-d0314tx.webp",
        "productName": "HP Victus 16-D0314TX Gaming Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹61,500",
        "rating": "4.75",
        "specScore": "71",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIdVy~-TST64ifGhrhArnrysuhyihDRPR_l.S.Z1h-hrhhaFhrhrhhacBrWahrhrBi5AFGBZiU2hrFB5SJfSsG79AAKz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixUnNaUSE-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ741WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹65,990",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI1-0z7pFq6BTbNhrhArnrysuhyihDRPw4doepXVh-hrhhaFhrhrhhacBrWahrhrBi5lON4O4QFhrFB5nPg6iQIxK9e5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivCTsHqDW-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ523WS Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹45,990",
        "rating": "4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw69QUjbKsVjYYPhrhArnrysuhyihDRPww1XZRVoh-hrhhaFhrhrhhacBrWahrhrBi5g4UlN6A5hrFB5bsPb.QYlRFP6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilCNAT0d8-w280-h280/hp-pavilion-15-eg307.webp",
        "productName": "HP Pavilion 15-eg3079TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹67,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 1340p",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzDBQB2UH8CB_RVhrhAgTYBOr3Uh7tBcBr2YTh3coPoZcYuUaTcAs3acY4c5ZUtcWauc5ZHPBc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54caWZPGlUCcUtYucTYWtUcTrBUshDhDh8Hrabl4XoXGiZbhmBYihkwkp71fSjp1V~f1~RhrhhaFhrhrhhacBrWahrhrBi5PrOa6PI6hrFB5lyJ~jOzifur6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNs8ukgdd-w280-h280/lenovo-v15-g4-82yu00.webp",
        "productName": "Lenovo V15 G4 ‎82YU00W7IN Laptop (AMD Ryzen 3 7320U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹27,980",
        "rating": "4.45",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqbRdZowVJjG_.FhrhArnrysuhyihDRPwbl.HzVJh-hrhhaFhrhrhhacBrWahrhrBi5PUlsG4N4hrFB5x7pu9y~isNkf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iibmHDw6n-w280-h280/apple-macbook-air-15.webp",
        "productName": "Apple MacBook Air 15 2023 Laptop (Apple M2/ 8GB/ 512GB SSD/ MacOS)",
        "price": "₹1,10,990",
        "rating": "4.75",
        "specScore": "54",
        "features": [
            "Apple M2",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "10-Core GPU",
            "15.3 inches, 2880 x 1864 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFw~sdewjYGafd6mpphrhAgTYBOr3Uh7rBBTacoPoZcnrA6ssOcrY3cnocXcW6c45ocW6cFFicnrAsFc2auUC3rcnNOUZtucrh-hDh8Xl6aoHrrilrA5hmBYihkwkp7~jo0Rd-l7zE~hrhhaFhrhrhhacBrWahrhrBi5uTuAo6YFhrFB5Eqi0DrROPIOo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icsZQE2tu-w280-h280/hp-pavilion-15s-fq51.webp",
        "productName": "HP Pavilion 15s-fq5190TU Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹66,490",
        "rating": "4.2",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI1rup8F~1yxs.JhrhArnrysuhyihDRPwZKllmz1h-hrhhaFhrhrhhacBrWahrhrBi5ZOWiAiZOhrFB5DTBGZaX-870z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ic0q8FcYS-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2023 K3605VC-MB542WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹75,990",
        "rating": "4.35",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA Geforce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFI1~ymn5DCAxlhrhArnrysuhyihDRPwZGRo0b~h-hrhhaFhrhrhhacBrWahrhrBi5us85I4IthrFB5A2nBuWspz2qi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijhz7SzjM-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HF-HN025W Gaming Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹53,854",
        "rating": "4.6",
        "specScore": "66",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI9z-CJmpu-uglGhrhArnrysuhyihDRPwoGeKlfvh-hrhhaFhrhrhhacBrWahrhrBi5IDtiF4Q3hrFB5YY30CIFDjgPk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iu94IIjtd-w280-h280/hp-victus-15-fb0106a.webp",
        "productName": "HP Victus 15-fb0106AX Gaming Laptop (Ryzen 5 5600H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹60,990",
        "rating": "4.35",
        "specScore": "64",
        "features": [
            "5th Gen AMD Ryzen 5 5600H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq~.TC-1swq_IB1hrhArnrysuhyihDRPRJelfdw_h-hrhhaFhrhrhhacBrWahrhrBi5gsssWlPZhrFB508yQuykD7wRE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVzBzPNpP-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82KU0238IN Laptop (AMD Ryzen 5 5500U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹38,990",
        "rating": "4.15",
        "specScore": "59",
        "features": [
            "5th Gen AMD Ryzen 5  5500U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90pdKAz1tiqE7XkhrhAgTYBOr3Uh7Taus2scYiarBricFTYnc5coPoHcrnic3Iyauc4ctaDrcAs3ac44PPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54rTAGcUtYucTYWtUcTrBUshDhDh8HrbPZ4g4PooGPhmBYihkwkp7dofKex77_f7ZhrhhaFhrhrhhacBrWahrhrBi5tsTrlYZrhrFB5gVFdRPgYOu3a"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1H8OjYwD-w280-h280/dell-vostro-3520-lap.webp",
        "productName": "Dell Vostro 3520 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹46,990",
        "rating": "4.2",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw6OBYU2E.z.kb~hrhArnrysuhyihDRPwe7H75X7h-hrhhaFhrhrhhacBrWahrhrBi5rTrIBPgIhrFB5Zkegrqr5PJo8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1251Kx0x-w280-h280/hp-pavilion-15s-fr50.webp",
        "productName": "HP Pavilion 15s-FR5007TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹47,490",
        "rating": "4.6",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK40_PJzREygR4ophrhAA3snrh7tBcYuUaTcg34PPGUCcAs3acY4c5oUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAactsnachYcFUCiauUcoPo5cYuUaTcY3YFcDacgCTTcticYBFciYFBTrIcFYThCcbB5ZPBrcrAQch-hDo4lHGZhrhhaFhrhrhhacBrWahrhrBi52lAyTBaQhrFB5P_CzHIeIqQyO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAKMUE8VT-w280-h280/hp-15s-eq2143au-lapt.webp",
        "productName": "HP 15s-eq2143au Laptop (Ryzen 3 5300U/ 8GB/ 512GB SSD/ Windows 11 Home)",
        "price": "₹29,990",
        "rating": "4.55",
        "specScore": "50",
        "features": [
            "5th Gen AMD Ryzen 3  5300U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xnNnJls4Pmlr8ChrhArnrysuhyihDRPlv5pppzSh-hrhhaFhrhrhhacBrWahrhrBi5OIrXt6iXhrFB52n.3iB3zD395"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7KmiNI47-w280-h280/dell-vostro-3481-lap.webp",
        "productName": "Dell Vostro 3481 Laptop (8th Gen Core i5/ 8GB/ 1TB/ Linux/ 2GB Graph)",
        "price": "₹46,790",
        "rating": "4.65",
        "specScore": "54",
        "features": [
            "8th Gen Intel Core i5 8265U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "2 GB AMD Radeon 520",
            "14 inches, 1366 x 768 pixels",
            "Linux OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYl9fvgg7tIPVorhrhAgTYBOr3Uh7iaTTc2sFU3sc5HcZPPPcYuUaTcAs3acY4cXUtcWaucXob4CcXcW6c5cU6ctiicTYuCDcocW6cW3rBtYAFc2sFcZHXPcTrBUshDhDh8ZbrlPb5gAlG6rhmBYihkwkpxSzSv17ejlK..hrhhaFhrhrhhacBrWahrhrBi5FCtulBoZhrFB5nKnU-V6mo6Qy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEFytCIeV-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2024 MXCV3HN/A Laptop (Apple M3/ 16GB/ 256GB SSD/ MacOS)",
        "price": "₹1,34,900",
        "rating": "4.05",
        "specScore": "50",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "16 GB  RAM",
            "256 GB SSD",
            "Apple 10 Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG0RfYJrw6sNytGBhrhAgTYBOr3Uh7rBBTacnrA6ssOcrY3cnZc5bcW6co4bcW6cFFicnrAsFcFsusnrcnDA2Ztucrh-hDh8alPgaZlG5laPahmBYihkwkpSoe.xGSS-xxE-hrhhaFhrhrhhacBrWahrhrBi5tFHXnaNahrFB5.tZsZBXux-gn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imroP0Wqc-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED S5504VA-MA943WS Laptop (13th Gen Core i9/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹86,990",
        "rating": "4.75",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYJ2TsJuq5U55FthrhAgTYBOr3Uh7rFCFc2Y2s6ssOcFc54csTaicYuUaTcAs3acYlc5ZUtcWauc5ZlPPtc5bcW6c45ocW6cFFic8Yuis8Fc55cB3scF44PH2rcnrlH58FcUtYucTYWtUcTrBUshDhDh8bblGHlGbAa5oAhmBYihkwkpSZR7RV1xK7lzvhrhhaFhrhrhhacBrWahrhrBi5HD5ZuGGChrFB57-Ga-T3K1ybU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaqYZYPMN-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS13J00 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹89,990",
        "rating": "4.1",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKPWPAf1dRuHPmuhrhArnrysuhyihDRPKl~1-HJlh-hrhhaFhrhrhhacBrWahrhrBi55y6BiYy6hrFB5Dgx06TrgBYYx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizWzm3cu-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-79G UN.34NSI.002 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,990",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY7AdT25EXdb5rGhrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrG54cGlWcWrnhNcTrBUshDhDh8XoPX5PoAlGgllhmBYihkwkpSZ7lb-Gwqb.1ShrhhaFhrhrhhacBrWahrhrBi5rY2B36l6hrFB5fpqYlTNnQJKR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iW7dwSzMw-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA506NFR-HN045W Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹66,990",
        "rating": "4.35",
        "specScore": "63",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwu_S~G~JQe6AXDhrhArnrysuhyihDRPwK~4wJl0h-hrhhaFhrhrhhacBrWahrhrBi5TNCDUtHZhrFB5PCVG-PzfPlNr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4xVTkqLi-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA566NC-HN083WS Laptop (AMD Ryzen 5 7535HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹67,990",
        "rating": "4.4",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3-YroATFok~UNShrhAA3snrh7rFCFcUCgcWrnhNcr54crnic3Iyauc4cWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAactsnachYcFUCiauUcW3rBthschncocZcOWch-hDZPbbG4hrhhaFhrhrhhacBrWahrhrBi5PoX2WAHBhrFB5lb7Nvkbql1mE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPPbI4GRG-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QSIN Laptop (AMD Ryzen 7 7735HS / 16GB/ 512GB SSD/ Win11/ 6GB Graph RTX 3050)",
        "price": "₹72,990",
        "rating": "4.5",
        "specScore": "68",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq_dR~ks3BOFryShrhArnrysuhyihDRPKXS_J-xVh-hrhhaFhrhrhhacBrWahrhrBi5aI4itaZihrFB5pSiWSwRYEQbb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMi9Wylzb-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JFA02NIN Laptop (AMD Ryzen 7 7730U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹48,490",
        "rating": "4",
        "specScore": "65",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq9x78DKKas1X27hrhArnrysuhyihDRPwJm_volxh-hrhhaFhrhrhhacBrWahrhrBi5WQ6i2gUyhrFB5CQD~aJ3gJ9DG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGxLaMYxX-w280-h280/lenovo-ideapad-pro-5.webp",
        "productName": "Lenovo IdeaPad Pro 5 83D2001GIN Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,09,990",
        "rating": "4",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Integrated Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sggvmknD7qirq9VChrhAA3snrh7Taus2scYiarBricB3sc4YcYuUaTcAs3acCTU3rclc5HUtcWaucUtYuchYcTYWtUcTrBUsBcZoW6c5U6cFFic8Yuis8Fc55cB3sc5HcYuAtcsTaiciYFBTrIcr3AUYAcW3aIc5cHbcOWch-hDZPbZZZhrhhaFhrhrhhacBrWahrhrBi5YOgGFrQGhrFB5Ng4NOUdj42Qs"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip5f77LMo-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 83DA003GIN Laptop (Intel Core Ultra 5 125H/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹81,490",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw8FePrzEdUur1YhrhArnrysuhyihDRPwf7.eRv0h-hrhhaFhrhrhhacBrWahrhrBi5TXsbINo2hrFB5vYoVDu0a_tCT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuuzEUvTp-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹39,990",
        "rating": "4.45",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9T~pZZD~7xbNICZhrhAgTYBOr3Uh7rAa3crFBY3acThscrnic3IyaucGcsAUrcAs3ac4GPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54cH5cUtYucTYWtUcTrBUshDhDh855iAoG4ZPGagHhmBYihkwkpSfGH-0JJSVJVjhrhhaFhrhrhhacBrWahrhrBi5iC3aaNn4hrFB5i_goOI-P1J30"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2US2dZgf-w280-h280/colorful-evol-p15-ga.webp",
        "productName": "Colorful Evol P15 Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹78,990",
        "rating": "4.55",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYv8Qiktx0~-n95hrhAgTYBOr3Uh7AsTs3gCTcB54cYuUaTcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPcoZctgGb65b45oac8cYuicWrnhNcTrBUshDhDh8XrrrGA56or6obhmBYihkwkp7.VxRVSxR_SeVhrhhaFhrhrhhacBrWahrhrBi5TBHsI6YuhrFB5gkVSzXEK7CyS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2ZY1egVH-w280-h280/msi-thin-a15-ai-b7ve.webp",
        "productName": "MSI Thin A15 AI B7VE-065IN Gaming Laptop (AMD Ryzen 7 7735H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹79,990",
        "rating": "4.25",
        "specScore": "73",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOXlFDTz~1dYTHKhrhAgTYBOr3Uh7nFYcUtYucr54crnic3IyaucGcsAUrcAs3acGGZ4tFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc6G2acPb4YucWrnhNcTrBUshDhDh8b5HPPAoaibXPohmBYihkwkp7_pe_70So~.S.hrhhaFhrhrhhacBrWahrhrBi5syI523CuhrFB5yjVbZeEtQ11f"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSX7KGO7P-w280-h280/msi-thin-a15-ai-b7vf.webp",
        "productName": "MSI Thin A15 AI B7VF-064IN Gaming Laptop (AMD Ryzen 7 7735H/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹93,990",
        "rating": "4.35",
        "specScore": "75",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqQ6YDpljOPGER4hrhArnrysuhyihDRPw04K4dJeh-hrhhaFhrhrhhacBrWahrhrBi5OuDPanNNhrFB5PoS7zAUInKWU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHFtSTOks-w280-h280/hp-pavilion-plus-14.webp",
        "productName": "HP Pavilion Plus 14-ew0116TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹68,990",
        "rating": "4",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67lDrHNIFJEwNFqhrhArnrysuhyihDRPwJKR-Z~Xh-hrhhaFhrhrhhacBrWahrhrBi5sQyXgOiyhrFB5mq2WCa9rrqqQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iclisoaGK-w280-h280/asus-tuf-f17-fx706hf.webp",
        "productName": "Asus TUF F17 FX706HF-NY040W Gaming Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹50,990",
        "rating": "4.65",
        "specScore": "63",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR6 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GqR~Dr1OdkP38bhrhAA3snrh7rFCFcUCgcWrnhNcg5GcYuUaTcAs3acY4c55UtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc5GcYuAtc5b4ctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcoP4PcW3rBthschncocGlcOWch-hDZPZ4PlhrhhaFhrhrhhacBrWahrhrBi56aXTBiGthrFB5smQWU2x8_EDH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ij0HJKEi5-w280-h280/dell-g15-5530-gn5530.webp",
        "productName": "Dell G15-5530 GN5530D83M6001ORB1 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹70,719",
        "rating": "4.4",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PX6nma-KCiVSwJhrhArnrysuhyihDRPKRmVz7Zwh-hrhhaFhrhrhhacBrWahrhrBi5gli5U8TXhrFB5wmkWrKtxm1xE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJUFU814v-w280-h280/honor-magicbook-x16.webp",
        "productName": "Honor MagicBook X16 2024 ‎Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹49,717",
        "rating": "4.1",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwi5fmafq94wEuwhrhArnrysuhyihDRPwv~RHSR1h-hrhhaFhrhrhhacBrWahrhrBi5iBgPNIO3hrFB5GAyCz-VpYVlr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip9x4p8qy-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 15IAH8 83ER008HIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹54,390",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZC7Qk5vp43wXQahrhAA3snrh7Taus2scYiarBricFTYncZc54YrtXcYuUaTcAs3acY4c5oUtcWaucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5cr3AUYAcW3aIc5cbocOWch-hDZPZHo5hrhhaFhrhrhhacBrWahrhrBi5iPIXQrOXhrFB5bO_xix~EqK02"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5lcPQlPn-w280-h280/infinix-inbook-y4-ma.webp",
        "productName": "Infinix INBook Y4 Max Series YL613 Laptop (13th Gen Core i3/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹33,990",
        "rating": "4.45",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQtF~fU0Qe81xrShrhAgTYBOr3Uh7YugYuYDcIHcnrDcFa3YaFcYuUaTcAs3acYZc5ZUtcWauc5Z54Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacITb5ZcUtYucTYWtUcTrBUshDhDh8bGi6ligo4roH5hmBYihkwkp7JJKSlJ7wSSq7hrhhaFhrhrhhacBrWahrhrBi585D8Ui2thrFB5APXHm5v162YV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivp89KnId-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 1 82R400BGIN Laptop (AMD Ryzen 5 5500U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹33,990",
        "rating": "4.6",
        "specScore": "46",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "8 GB  DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFqFnw1bwu5gnnbhrhAgTYBOr3Uh7Taus2scrnic3Iyauc4c3IyaucXcW6c45ocW6cFFic8Yuis8Fc55ctsnacXo3HPP6WYucUtYucTYWtUcTrBUshDhDh8XZbggZoGog5ZZhmBYihkwkp7zzRxwfVES~q7hrhhaFhrhrhhacBrWahrhrBi5iGn4AyWFhrFB5e6zUs7XTnog4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iItJKshN3-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Max/ 48GB/ 1TB SSD/ macOS)",
        "price": "₹3,79,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "Apple M3 Max",
            "16 Cores (12P + 4E)",
            "48 GB  RAM",
            "1 TB SSD",
            "40 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NEX9OqoXTT3l3CihrhArnrysuhyihDRPwp4e.Gw1h-hrhhaFhrhrhhacBrWahrhrBi5tuiZOHunhrFB5JI5tpePT.H1R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijEF5B35u-w280-h280/dell-inspiron-7430-2.webp",
        "productName": "Dell Inspiron 7430 2 in 1 2023 Laptop (13th Gen Core i3/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹47,990",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqSDyZ7tgEVR4tQhrhArnrysuhyihDRPw-V5Z0-fh-hrhhaFhrhrhhacBrWahrhrBi54WXInsoUhrFB5d4e9mJaZv5IF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irgfVN7iQ-w280-h280/lenovo-legion-slim-5.webp",
        "productName": "Lenovo Legion Slim 5 82Y9009KIN Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹99,990",
        "rating": "4.4",
        "specScore": "75",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqnVSDubukxTyqRhrhArnrysuhyihDRPw7mv0Sbwh-hrhhaFhrhrhhacBrWahrhrBi5aGT52iZlhrFB5dDjeqn546dxn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iO01rBeU7-w280-h280/lenovo-loq-15irh8-82.webp",
        "productName": "Lenovo LOQ 15IRH8 82XV00F7IN 2023 Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹82,990",
        "rating": "4",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90ubT34wgmY1JGNhrhAgTYBOr3Uh7Taus2scTsNcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc54Y3tXiocWrnhNcTrBUshDhDh8aPl5ib5PZio6ZhmBYihkwkp7vx0RwS1_Ed04hrhhaFhrhrhhacBrWahrhrBi56B6A3Y3ahrFB5.~SdCRZ84Yn0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixUnNaUSE-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ741WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹65,990",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI1-0z7pFq6BTbNhrhArnrysuhyihDRPw4doepXVh-hrhhaFhrhrhhacBrWahrhrBi5lON4O4QFhrFB5nPg6iQIxK9e5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNs8ukgdd-w280-h280/lenovo-v15-g4-82yu00.webp",
        "productName": "Lenovo V15 G4 ‎82YU00W7IN Laptop (AMD Ryzen 3 7320U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹26,990",
        "rating": "4.45",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFjmB3PB0o6rSW8hrhAgTYBOr3Uh7Taus2sc254crnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacWHcrnuc5cUtYucTYWtUcTrBUshDhDh84X5lHP5GHZaoGhmBYihkwkp71fV.jJfXE_bwhrhhaFhrhrhhacBrWahrhrBi5PUlsG4N4hrFB5PXbJCspYG2VT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i66WzFcoY-w280-h280/dell-inspiron-5630-l.webp",
        "productName": "Dell Inspiron 5630 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹68,719",
        "rating": "4.6",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 1340P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwsm2uvemA~eodQhrhArnrysuhyihDRPKRm-VKl.h-hrhhaFhrhrhhacBrWahrhrBi5ZBaBHXDshrFB5rHq_~jFu29yl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iibmHDw6n-w280-h280/apple-macbook-air-15.webp",
        "productName": "Apple MacBook Air 15 2023 Laptop (Apple M2/ 8GB/ 512GB SSD/ MacOS)",
        "price": "₹1,10,990",
        "rating": "4.75",
        "specScore": "54",
        "features": [
            "Apple M2",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "10-Core GPU",
            "15.3 inches, 2880 x 1864 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFw~sdewjYGafd6mpphrhAgTYBOr3Uh7rBBTacoPoZcnrA6ssOcrY3cnocXcW6c45ocW6cFFicnrAsFc2auUC3rcnNOUZtucrh-hDh8Xl6aoHrrilrA5hmBYihkwkp7~jo0Rd-l7zE~hrhhaFhrhrhhacBrWahrhrBi5uTuAo6YFhrFB5Eqi0DrROPIOo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBfuDJxSK-w280-h280/hp-victus-15-fa0555t.webp",
        "productName": "HP Victus 15-fa0555TX  Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹66,990",
        "rating": "4.25",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqz9VCOd~NEwGrJhrhArnrysuhyihDRPwwf5z4Zlh-hrhhaFhrhrhhacBrWahrhrBi5aiTD6toshrFB5jRdzf55Ysx5P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivnzUtff7-w280-h280/hp-15s-fr5009tu-lapt.webp",
        "productName": "HP 15s-fr5009TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.05",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK41pEnj2~Oioi0bhrhAA3snrh7tBc54Fcg34PPlUCcYuUaTcAs3acYZc5oUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5cYuUaTcCticgticiYFBTrIcurUC3rTcFYThCcGNbylBrch-hDoGo4ZHhrhhaFhrhrhhacBrWahrhrBi5gUsPWgithrFB5b-5iVpyU_~Ew"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5N4UYgEt-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 PHN16-71 2023 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,54,990",
        "rating": "4.25",
        "specScore": "74",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9B2HimY~W-fVRtBdhrhArnrysuhyihDRPwwv04HfGh-hrhhaFhrhrhhacBrWahrhrBi5Qo2F2g63hrFB5UfNglQ-rC2gw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ic0q8FcYS-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2023 K3605VC-MB542WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹75,990",
        "rating": "4.35",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA Geforce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFI1~ymn5DCAxlhrhArnrysuhyihDRPwZGRo0b~h-hrhhaFhrhrhhacBrWahrhrBi5us85I4IthrFB5A2nBuWspz2qi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGgkJ0ep2-w280-h280/msi-cyborg-15-a12ucx.webp",
        "productName": "MSI Cyborg 15 A12UCX-264IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹54,990",
        "rating": "4.6",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Nvidia GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpE2kaIdqO7rnUhrhArnrysuhyihDRPwZS.XomSh-hrhhaFhrhrhhacBrWahrhrBi54s6rbD8YhrFB5k9xP_gj55DN6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilWxbzBLm-w280-h280/msi-stealth-17-a13vh.webp",
        "productName": "MSI Stealth 17 A13VH-055IN Gaming Laptop (13th Gen Core i9/ 64GB/ 2TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹4,39,990",
        "rating": "4.7",
        "specScore": "98",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "64 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB Nvidia GeForce RTX4080",
            "17.3 inches, 3840 x 2160 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREv_-KKXCkIvuXVoeohrhArnrysuhyihDRPRJVZze5wh-hrhhaFhrhrhhacBrWahrhrBi52FWC3QrPhrFB50X1lUJWOZptO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTa4oYnIZ-w280-h280/hp-240-g8-689u3pa-bu.webp",
        "productName": "HP 240 G8 689U3PA Business Laptop (11th Gen Core i5/ 8GB/ 512 GB SSD/ Win11)",
        "price": "₹37,890",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQQaiCiOFou.o0lhrhAgTYBOr3Uh7tBcWXcFa3YaFcYuUaTcAs3acY4c55UtcWaucYuUaTcAs3acY4c55Z4WcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacoHPc6CFYuaFFcTrBUshDhDh8ZZiHAA4gbZa5ohmBYihkwkp7pEG_q-dKdxd0hrhhaFhrhrhhacBrWahrhrBi5Fu5TW4GBhrFB5Gdk~d8dg.H5i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYLTSDXiG-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-41 NX.KG3SI.006 Laptop (AMD Ryzen 5 7430U / 16GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹44,990",
        "rating": "4.3",
        "specScore": "60",
        "features": [
            "7th Gen AMD Ryzen 5 7430U",
            "Hexa Core, 12 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYXeWOAXARAXJ~BhrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcoPoHcrnic3Iyauc4ctaDrcAs3acGHZPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFgW5HcH5cUtYucTYWtUcTrBUshDhDh8gHXZi4545PXb6hmBYihkwkpSZ7xdVpS-qRfxhrhhaFhrhrhhacBrWahrhrBi5aCTCNDoGhrFB5Q008sOg2Pn_-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVQ2IRowv-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-41 NX.KG3SI.007 Laptop (AMD Ryzen 7 7730U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹49,990",
        "rating": "4",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjQl2-7IZBR7I1hrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcoPoHcrnic3IyaucGcsAUrcAs3acGGZPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFgW5HcH5cUtYucTYWtUcTrBUshDhDh8XAoHriroliZlXhmBYihkwkpSZ7xd..7~zjqJhrhhaFhrhrhhacBrWahrhrBi52brysTAUhrFB5w42KyTarqJkU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTMOBmuHR-w280-h280/acer-aspire-3-a324-3.webp",
        "productName": "Acer Aspire 3 A324-31 Laptop (Intel Core i3 N305/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹27,990",
        "rating": "4.75",
        "specScore": "46",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtIoJfAGkpaX7QDhrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAs3acYZc5oUtcWaucuZP4cXcW6c45ocW6cFFic8Yuis8Fc55ctsnacrZoHcZ5cUtYucTYWtUcTrBUshDhDh8bg4HggPlrPXXrhmBYihkwkpSoqR.~0wxVEGzhrhhaFhrhrhhacBrWahrhrBi5UFDH5sNXhrFB5ndxRtqHUiEZD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izvT2kfdD-w280-h280/dell-15-vostro-3520.webp",
        "productName": "Dell 15 Vostro 3520 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹37,490",
        "rating": "4.6",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwJXUTIWJg1FWYxhrhArnrysuhyihDRPKXZoxJ._h-hrhhaFhrhrhhacBrWahrhrBi5GBY8PPIlhrFB5YH4QAXC-o6bk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAMLtuf7b-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS1FQ00 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹68,990",
        "rating": "4.75",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwsvz464H7aAOA3hrhArnrysuhyihDRPKwbevzz4h-hrhhaFhrhrhhacBrWahrhrBi5F5no3WgshrFB53~6e96x98Qkp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3QJHb2I0-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XF007FIN Laptop (13th Gen Core i7/ 16GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹81,690",
        "rating": "4",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI.R43UpyY6kA8AhrhArnrysuhyihDRPKlSo_R0mh-hrhhaFhrhrhhacBrWahrhrBi5Q8XWFABPhrFB5yROJ6BxqYY6G"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5jZtSDav-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00PQIN Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050)",
        "price": "₹75,990",
        "rating": "4",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HbYqNxlVX39glOhrhAA3snrh7Taus2scTsNc54Y3DlcYuUaTcAs3acY4c5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoPo5cTCurcW3aIcocZXcOWch-hDZPGHZXhrhhaFhrhrhhacBrWahrhrBi5Wa88ZuZGhrFB5pOZBvdC5WYb8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izCELdc7r-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA566NCR-HN075W Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹71,990",
        "rating": "4.15",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYknHuKCp4XZJQ1hrhAgTYBOr3Uh7rFCFcUCgcWrnhNcr54crnic3IyaucGcsAUrcAs3acGHZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcgr4bbuA3ctuPG48cTrBUshDhDh8gX4aabbAr6GZ4hmBYihkwkpSxzodf40GvwpVhrhhaFhrhrhhacBrWahrhrBi5Hr4PI6tOhrFB5OvJw1d3_8XFe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizh9GqQ2-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA566NFR-HN259W Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹62,990",
        "rating": "4.15",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY-V8nmybnAOJiKhrhAgTYBOr3Uh7rFCFcUCgcWrnhNcr54crnic3IyaucGcsAUrcAs3acGHZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pcgr4bbug3ctuo4l8cTrBUshDhDh8oGHXarG4ZXA4PhmBYihkwkpSxzodqJ7fKJj0hrhhaFhrhrhhacBrWahrhrBi5ZbZy8WIZhrFB5Nol7Hrgvp7Nt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqUUmyuh9-w280-h280/hp-14-gr1023tu-lapto.webp",
        "productName": "HP 14-gr1023TU Laptop (Intel Core Ultra i7 155H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹81,999",
        "rating": "4.75",
        "specScore": "64",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Integrated Intel Arc",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GJ--zfojqF2j8rhrhAA3snrh7tBc5HcW35PoZUCcYuUaTcAs3acCTU3rcGcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCcrTCnYuCnc5cHcOWch-hDZPG4blhrhhaFhrhrhhacBrWahrhrBi5ATPD6yulhrFB53UxGqI1ymT-j"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifxJH7EZt-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 3 NP754XFG-KB1IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹64,990",
        "rating": "4.1",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwni4OiTyjEROruhrhArnrysuhyihDRPw7lX_mGph-hrhhaFhrhrhhacBrWahrhrBi5Ho584GAshrFB5.p1TQ3HJS9Eg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNRDAyTDR-w280-h280/dell-inspiron-5445-l.webp",
        "productName": "Dell Inspiron 5445 Laptop (AMD Ryzen 5 8540U/ 16GB/ 512GB SSD/ Windows 11 Home)",
        "price": "₹65,990",
        "rating": "4.6",
        "specScore": "64",
        "features": [
            "8th Gen AMD Ryzen 5 8540U",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HPBPyiksH-dCfohrhAA3snrh7iaTTcYuFBY3suc4HH4crnic3Iyauc4cX4HPcCcXUtcWaucUtYucTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgticBTCFciYFBTrIcnFcsggYAacoPo5cYAac6TCac5cb5cOWch-hDZPGGP5hrhhaFhrhrhhacBrWahrhrBi5sgUBZbyPhrFB5bYOyT77nya35"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJ4DMFKfH-w280-h280/dell-inspiron-5445-l.webp",
        "productName": "Dell Inspiron 5445 Laptop (AMD Ryzen 7 8840U/ 16GB/ 1TB SSD/ Windows 11 Home)",
        "price": "₹72,599",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "8th Gen AMD Ryzen 7 8840U",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0H4K~J.DV69C3N7hrhAA3snrh7iaTTcYuFBY3suc4HH4crnic3IyaucGcXXHPCcXUtcWaucUtYucTYWtUcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnac5HcYuAtcgticBTCFciYFBTrIcnFcsggYAacoPo5cYAac6TCac5cb5cOWch-hDZPGGPohrhhaFhrhrhhacBrWahrhrBi5ZgOorNoghrFB5lgTNNDPmZOgI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4aIixHlF-w280-h280/lenovo-ideapad-3-14i.webp",
        "productName": "Lenovo IdeaPad 3 14IAU7 82RJ00FFIN Laptop (12th Gen Core i3/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹42,990",
        "rating": "4.1",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYGf04XEHiJ251uhrhAgTYBOr3Uh7Taus2scYiarBricZcYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HYrCGcUtYucTYWtUcTrBUshDhDh8bgZoaloXAg5AGhmBYihkwkpSxf.Z7_x.VfddhrhhaFhrhrhhacBrWahrhrBi5IU3sCiOWhrFB5GRjfDFqiHdwU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPPbI4GRG-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QSIN Laptop (AMD Ryzen 7 7735HS / 16GB/ 512GB SSD/ Win11/ 6GB Graph RTX 3050)",
        "price": "₹72,990",
        "rating": "4.5",
        "specScore": "68",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq_dR~ks3BOFryShrhArnrysuhyihDRPKXS_J-xVh-hrhhaFhrhrhhacBrWahrhrBi5aI4itaZihrFB5pSiWSwRYEQbb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijmUr7Z1j-w280-h280/msi-katana-a17-ai-b8.webp",
        "productName": "MSI Katana A17 AI B8VE-884IN Gaming Laptop (AMD Ryzen 9 8945HS/ 16GB/ 1TB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹1,14,990",
        "rating": "4.65",
        "specScore": "75",
        "features": [
            "8th Gen AMD Ryzen 9 8945HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJEb5PQ7U2kCDzoThrhArnrysuhyihDRPR057R_V1h-hrhhaFhrhrhhacBrWahrhrBi5TsCbiW4YhrFB52Xl2I3gEjN5Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icr0cFt3E-w280-h280/colorful-evol-p15-23.webp",
        "productName": "Colorful Evol P15 23-HE55D16512A-G-IND Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹63,990",
        "rating": "4.25",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY-uoA4sdfgpSXQhrhAgTYBOr3Uh7AsTs3gCTca2sTcB54cYuUaTcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4PcoZcta44i5b45orcWcYuicWrnhNcTrBUshDhDh8iaPoZ4a44GHPghmBYihkwkpSx1dfS.fRxXwxhrhhaFhrhrhhacBrWahrhrBi5WyWBa8CQhrFB5bNp7.5o.I08P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7nDRfKv9-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QKIN Laptop (AMD Ryzen 5 7535HS / 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹64,990",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqeklx7YU9kIA.EhrhArnrysuhyihDRPKXSJ5Z_1h-hrhhaFhrhrhhacBrWahrhrBi5guANHXCQhrFB5vD.BVizA~dP9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijAZU7Erx-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA506NCR-HN054W Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹69,520",
        "rating": "4.45",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwsQOBdAv9wIkHmhrhArnrysuhyihDRPKl-m-ozSh-hrhhaFhrhrhhacBrWahrhrBi58FPonbsghrFB51zBGTrW7oO5s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7gAf1eB5-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA506NC-HN083W Laptop (AMD Ryzen 5 7535HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹59,990",
        "rating": "4.75",
        "specScore": "63",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY7AdT25EXdb5rGhrhAgTYBOr3Uh7rFCFcUCgcWrnhNcr54crnic3Iyauc4ctaDrcAs3acG4Z4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcgr4PbuActuPXZ8cTrBUshDhDh85P45HaAiorGlHhmBYihkwkpSxVozZVwSVjxEhrhhaFhrhrhhacBrWahrhrBi5n5isBygDhrFB5-HmXjNdwSK0t"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6ufdKHmr-w280-h280/lenovo-legion-7-16ir.webp",
        "productName": "Lenovo Legion 7 16IRX9 83FD000XIN Gaming Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11/ 8GB RTX 4070 Graph)",
        "price": "₹2,08,490",
        "rating": "4.7",
        "specScore": "89",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_94JuG-1~Hj0z_RhrhArnrysuhyihDRPw__dHxKZh-hrhhaFhrhrhhacBrWahrhrBi5lC8F3b6bhrFB5EPz~Bml.n0-K"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibdebc0pV-w280-h280/hp-omen-16-xd0017ax.webp",
        "productName": "HP Omen 16-xd0017AX Gaming Laptop (AMD Ryzen 7 7840HS/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,25,990",
        "rating": "4.65",
        "specScore": "81",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 1080 x 1920 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ0~EXfopkmWEQtThrhArnrysuhyihDRPKbRxdeR4h-hrhhaFhrhrhhacBrWahrhrBi5IaIa3XHHhrFB5~NSlajS0OIpA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRxZz7ElP-w280-h280/infinix-zero-book-ul.webp",
        "productName": "Infinix Zero Book Ultra AI ZL514 Laptop ( Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹59,990",
        "rating": "4.55",
        "specScore": "60",
        "features": [
            "Intel Core Ultra 5 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated Intel Arc",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFeK4ajjNw9_mjOihrhAgTYBOr3Uh7YugYuYDcya3sc6ssOcCTU3rcrYcBAcYuUaTcAs3ac4c5o4tc5bcW6cFFic45ocW6cFFic8Yuis8Fc55ctsnacyT45HcUtYucTYWtUcTrBUshDhDh86llbGAiPZ4glohmBYihkwkpSxf.dE7E_Hf~_hrhhaFhrhrhhacBrWahrhrBi5FHi2T5GshrFB5.Go-s563DlfI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFck7SrFw-w280-h280/asus-zenbook-14-oled.webp",
        "productName": "Asus Zenbook 14 OLED 2024 UX3405MA-PZ962WS Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,44,990",
        "rating": "4.4",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXNSX4xYrFZsXu-~l9dhrhAgTYBOr3Uh7rFCFcyau6ssOc5HcsTaicoPoHcYuUaTcAs3acCTU3rclc5X4tcZocW6c5cU6cFFic8Yuis8Fc55ctsnacCDZHP4nrcBylbo8FcUtYucTYWtUcTrBUshDhDh8aPr4rll5ZZllHhmBYihkwkpSf7X.fpVR~_JlhrhhaFhrhrhhacBrWahrhrBi5B3G4TNushrFB5SIwfoopt833r"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFDFe06jN-w280-h280/hp-15s-fy5009tu-lapt.webp",
        "productName": "HP 15s-fy5009TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,021",
        "rating": "4",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwg0HytdEjC5KF8hrhArnrysuhyihDRPKHpbbxbvh-hrhhaFhrhrhhacBrWahrhrBi5uniWPAgghrFB5TKlxFdoev-fP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6DEjtfpN-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 UN.343SI.003 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹41,990",
        "rating": "4.55",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYGb1xkau3E-7CShrhAgTYBOr3Uh7rAa3crFBY3acZc6huTYUcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8HgrPgAgPaoa54hmBYihkwkpSfoHvp.X1EKzzhrhhaFhrhrhhacBrWahrhrBi5ZFbTQ2PAhrFB5~N~9DikE.nbw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKKXgdFPd-w280-h280/lenovo-loq-2024-15ah.webp",
        "productName": "Lenovo LOQ 2024 ‎15AHP9 83DX000MIN Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,11,850",
        "rating": "4.65",
        "specScore": "77",
        "features": [
            "8th Gen AMD Ryzen 7 8845HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXNSX5xYziK50a6B5g.hrhAgTYBOr3Uh7Taus2scTsNcrnic3IyaucGcsAUrcAs3acXXH4tFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc54rtBlcWrnhNcTrBUshDhDh8ZZ4HHrggHogPPhmBYihkwkpSxo-fGH7Sq17phrhhaFhrhrhhacBrWahrhrBi52obYuHlbhrFB5XfFfzHW1zaAg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iM02gv1D0-w280-h280/hp-victus-15-fa1312t.webp",
        "productName": "HP Victus 15-fa1312TX Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹56,990",
        "rating": "4.05",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYx7b7t_gsx7nZ.hrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4PtcXcW6c45ocW6cFFic8Yuis8Fc55cB3scHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54cgr5Z5oUDcWrnhNcTrBUshDhDh8HrH5A5gabZ46ghmBYihkwkpSfXV0wKd_0.SHhrhhaFhrhrhhacBrWahrhrBi5bZb3iUouhrFB52C7D9SGyQKH_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVBcQeSlB-w280-h280/asus-tuf-f17-fx706hf.webp",
        "productName": "Asus TUF F17 FX706HF-NY039W Gaming Laptop (11th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹60,990",
        "rating": "4.25",
        "specScore": "64",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR6 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq~.TC-1swq_A_~hrhArnrysuhyihDRPKZm.1eKGh-hrhhaFhrhrhhacBrWahrhrBi5uQnlr4oIhrFB5Gxkyjf6az-2S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQEPLT1pd-w280-h280/lenovo-loq-83gs000pi.webp",
        "productName": "Lenovo LOQ 83GS000PIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹70,880",
        "rating": "4",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwNg6IHljsdpDD2hrhArnrysuhyihDRPKH5wz4Jbh-hrhhaFhrhrhhacBrWahrhrBi5TGQDbr2ThrFB5bkuF7jToBKaG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPMkkmEro-w280-h280/hp-omen-16-wf1096tx.webp",
        "productName": "HP Omen 16-wf1096TX Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,35,370",
        "rating": "4.4",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BFa.FiR3uOWfsTYhrhArnrysuhyihDRPK5fmGofbh-hrhhaFhrhrhhacBrWahrhrBi5AB5Hb5W5hrFB5Xe0~U1xA8-X2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPMkkmEro-w280-h280/hp-omen-16-wf1096tx.webp",
        "productName": "HP Omen 16-wf1096TX Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,35,370",
        "rating": "4.4",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BFa.FiR3uOWfsTYhrhArnrysuhyihDRPK5fmGofbh-hrhhaFhrhrhhacBrWahrhrBi5AB5Hb5W5hrFB5Xe0~U1xA8-X2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHt5zhp6P-w280-h280/lenovo-legion-7-16ir.webp",
        "productName": "Lenovo Legion 7 16IRX9 83FD000YIN Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB RTX 4060 Graph)",
        "price": "₹1,74,990",
        "rating": "4.6",
        "specScore": "84",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_jVODZyr8UiTJm1hrhArnrysuhyihDRPw__XHR.0h-hrhhaFhrhrhhacBrWahrhrBi54NgtQgyThrFB5ofl-_8WnRJkz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icJEZzZeo-w280-h280/acer-al15g-52-2024-g.webp",
        "productName": "Acer ‎AL15G- 52 2024 Gaming Laptop (12th Gen Core i5-12450H/ 16GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹51,990",
        "rating": "4.15",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1ToqX8tkoSnIEhrhAgTYBOr3Uh7rAa3crTWcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrT54Wc4ocWrnhNcTrBUshDhDh8ZAbb4455abriZhmBYihkwkpSoz1ejX0KoH0-hrhhaFhrhrhhacBrWahrhrBi5aPiUDyPghrFB5~zx4pBPn.-HP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6MAEu9Cr-w280-h280/lenovo-thinkbook-16.webp",
        "productName": "Lenovo ThinkBook 16 G6 21KHA081IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹55,990",
        "rating": "4.45",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Iris Xe Graphics",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwtRDQTNQ3IFOE6hrhArnrysuhyihDRPKXoxH-pwh-hrhhaFhrhrhhacBrWahrhrBi5W4oUG8XahrFB5VoRQxQOp0rOd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inO4sAHoL-w280-h280/msi-thin-15-b12uc-16.webp",
        "productName": "MSI Thin 15 B12UC-1691IN Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX3050 Graph)",
        "price": "₹66,990",
        "rating": "4.7",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqz9VCOd~3dkN1ihrhArnrysuhyihDRPw0l-5~e-h-hrhhaFhrhrhhacBrWahrhrBi5siIgtNYghrFB5EtRApuVS9RRe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iycL490Rj-w280-h280/msi-thin-15-b12uc-16.webp",
        "productName": "MSI Thin 15 B12UC-1692IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX3050 Graph)",
        "price": "₹57,990",
        "rating": "4.4",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqd3wUFeR_IUGEVhrhArnrysuhyihDRPw0l1oRRXh-hrhhaFhrhrhhacBrWahrhrBi5ZF45bZP3hrFB57P0vetPqx0gG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIdOO2SJF-w280-h280/hp-15-fd0187tu-lapto.webp",
        "productName": "HP 15-fd0187TU Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,990",
        "rating": "4.2",
        "specScore": "50",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzBWosiPKPlFooohrhAgTYBOr3Uh7tBcYuUaTcAs3acY4c5ZUtcWauc5ZZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54cgiP5XGUCcUtYucTYWtUcTrBUshDhDh8XrGHP5HH5Po5ghmBYihkwkpSxw7R_4f7..7jhrhhaFhrhrhhacBrWahrhrBi5UG3BgUXNhrFB5zJFm~ABtsZ2e"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixAdr32h3-w280-h280/hp-victus-15-fa0444t.webp",
        "productName": "HP Victus 15-fa0444TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB RTX 3050)",
        "price": "₹66,990",
        "rating": "4.7",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYmlVG-9RFuRJgShrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55cB3scHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgrPHHHUDcWrnhNcTrBUshDhDh8lgAX5o5aHGl44hmBYihkwkpSfXV0_-p4S.7whrhhaFhrhrhhacBrWahrhrBi52Xa6OXN8hrFB5G9w2ojR6KNbT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJd2TTEJp-w280-h280/hp-victus-15-fa1227t.webp",
        "productName": "HP Victus 15-fa1227TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ RTX 2050)",
        "price": "₹59,500",
        "rating": "4",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqk6x3psKQKu37WhrhArnrysuhyihDRPKoKK-b1-h-hrhhaFhrhrhhacBrWahrhrBi5s5tZYaDZhrFB5Ss-e2NSl1vIz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iI7g7jG1u-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 2024  FA507UI-LP066WS Gaming Laptop (AMD Ryzen 9 8945H/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,41,990",
        "rating": "4.55",
        "specScore": "75",
        "features": [
            "9th Gen AMD Ryzen 9 8945H",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgQA_K22Nfu2ISJehrhAA3snrh7rFCFcUCgcrnic3IyaulcWrnhNcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55cXW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcHPGPcnFcsggYAacnaAtrcW3rIcococOWch-hDZPbHG4hrhhaFhrhrhhacBrWahrhrBi5n6BsOBNthrFB5BGJEj~nxgsJO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHLUfRnhU-w280-h280/hp-victus-15-fa1307t.webp",
        "productName": "HP Victus 15-fa1307TX Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home/ RTX 2050)",
        "price": "₹66,990",
        "rating": "4.75",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF_CQxvB.Vux9GnhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54cgr5ZPGUDcWrnhNcTrBUshDhDh8iA5AHaG565PbHhmBYihkwkpSfR1-dRjVEvVKhrhhaFhrhrhhacBrWahrhrBi5aCCOQ22lhrFB5CBx5..SqsmgP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imx7TOO7S-w280-h280/infinix-inbook-y2-pl.webp",
        "productName": "Infinix INBook Y2 Plus XL29 Laptop (11th Gen Core i7/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹74,990",
        "rating": "4.4",
        "specScore": "55",
        "features": [
            "11th Gen Intel Core i7 1195G7",
            "Quad Core, 8 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY~Xp9vkj1xFnxDhrhAgTYBOr3Uh7YugYuYDcYu6ssOcIocBTCFcYuUaTcAs3acYGc55UtcWauc55l4WGc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacDTolcUtYucTYWtUcTrBUshDhDh8446ZAHoZgAiabhmBYihkwkp70-GSS7Sxdp7dhrhhaFhrhrhhacBrWahrhrBi5oi2l26N4hrFB5FlZZlbzdtm_y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikIKwQDxm-w280-h280/dell-inspiron-7440-l.webp",
        "productName": "Dell Inspiron 7440 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹97,590",
        "rating": "4.75",
        "specScore": "63",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphic",
            "14 inches, 2240 x 1400 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqTSemzwzTsaPS0hrhArnrysuhyihDRPwfm_.oXxh-hrhhaFhrhrhhacBrWahrhrBi5PoUTtH3XhrFB5R8Vv_9WP7IRK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFs6KHBME-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 NH.QPFSI.003 Gaming Laptop (AMD Ryzen 7 7735HS/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹72,990",
        "rating": "4.25",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY1qjADQA3jgSq2hrhAgTYBOr3Uh7rAa3cuYU3scrnic3IyaucGcsAUrcAs3acGGZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcru254cH5cWrnhNcTrBUshDhDh85ArPaAgGlbZ6ihmBYihkwkp7.dG.X0Gj7zjKhrhhaFhrhrhhacBrWahrhrBi5DGOybssXhrFB5TvVfaZR86_AB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXObWCRDP-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JFA02PIN Laptop (AMD Ryzen 3 7330U/ 8GB/ 512 GB SSD/ Win11)",
        "price": "₹30,540",
        "rating": "4.6",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 3 7330U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzAB2IP.mjN6fCwhrhAgTYBOr3Uh7Taus2scrnic3IyaucZcNCricAs3acGZZPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacUtYuO6ssOc54cW4cUtYucTYWtUcTrBUshDhDh85bHaAXa4666Z4hmBYihkwkp7f7oZSZwvjREzhrhhaFhrhrhhacBrWahrhrBi5OGZo4PDNhrFB5eXkwIPtfk3Em"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNA3nBre7-w280-h280/lenovo-legion-pro-5.webp",
        "productName": "Lenovo Legion Pro 5 83DF003NIN Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,54,980",
        "rating": "4.35",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HINQYFKRx~sQa6j9jrpPBhrhAgTYBOr3Uh7Taus2scTaWh3cB3sc4coPoHcYuUaTcAs3acYGc5HUtcWauc5Hb4PtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5bY3DlcWrnhNcTrBUshDhDh8obPXAlPiZXai6hmBYihkwkp7fex711.1vKXwhrhhaFhrhrhhacBrWahrhrBi5TCtGy5aGhrFB53oOd3Pp~IFDU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-io36GPCrk-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 ‎PHN16-72 Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,74,990",
        "rating": "4.05",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BD_ulgSkVw7GJVEhrhArnrysuhyihDRPw_1JGRv.h-hrhhaFhrhrhhacBrWahrhrBi5nAoWtygBhrFB5sSbyGUxe~NKe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEfg1pmtV-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 3 5300U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹29,990",
        "rating": "4.25",
        "specScore": "55",
        "features": [
            "5th Gen AMD Ryzen 3 5300U",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFRYGpq--pQ1_KEhrhAgTYBOr3Uh7rAa3crnic3IyaucZcNCricAs3ac4ZPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54cH5cUtYucTYWtUcTrBUshDhDh8i5GbHoib6GZrZhmBYihkwkpSoXEHJKxREV1ZhrhhaFhrhrhhacBrWahrhrBi5tBoFX3HChrFB5BCUjQfdp4f8E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikmfhfsKg-w280-h280/hp-15s-fq5327tu-lapt.webp",
        "productName": "HP 15s-fq5327TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹37,498",
        "rating": "4.4",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzgypt9xqPvi76whrhAgTYBOr3Uh7tBc54FcgN4PPGUCcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgN4ZoGUCcUtYucTYWtUcTrBUshDhDh8PrGoXrblr44oPhmBYihkwkp7fS14pwqf.Se0hrhhaFhrhrhhacBrWahrhrBi5TPUZPI5UhrFB5Hxi.rvA~8xG1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilr8gTMSU-w280-h280/lenovo-v14-g3-82tsa0.webp",
        "productName": "Lenovo V14 G3 82TSA0EMIH Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹29,990",
        "rating": "4",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz6RobI_fwsk5TJhrhAgTYBOr3Uh7Taus2sc25HcWZcgticYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacTrBUshDhDh8aH6roGbg5GZbahmBYihkwkpSZRw~p7ZSx700hrhhaFhrhrhhacBrWahrhrBi5DP3rtYaUhrFB5_yVXyP72SA.i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icbt8fGxV-w280-h280/msi-thin-a15-ai-b7ve.webp",
        "productName": "MSI Thin A15 AI B7VE-066IN Gaming Laptop (AMD Ryzen 5 7535H/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹71,990",
        "rating": "4.5",
        "specScore": "71",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOH_XSN37KoNTP4hrhAgTYBOr3Uh7nFYcUtYucr54crnic3Iyauc4ctaDrcAs3acG4Z4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc6G2acPbbYucWrnhNcTrBUshDhDh8Pr6P6ria6olbGhmBYihkwkp7_pe_jxqfejwvhrhhaFhrhrhhacBrWahrhrBi5Z5PDNuXWhrFB5UsGjsdovFGkw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6JpW7cFK-w280-h280/hp-14s-dq5138tu-lapt.webp",
        "productName": "HP 14s-dq5138tu Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,999",
        "rating": "4.75",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JU8PqVaHJbFN.xjhrhAgTYBOr3Uh7tBcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HFciN45ZXUCcUtYucTYWtUcTrBUshDhDh8GAlo554HZi4lHhmBYihkwkp7fw1-b0Sv7fzohrhhaFhrhrhhacBrWahrhrBi5YAWFtlQ5hrFB5xv3YQYXQD6~T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0qPbIdq9-w280-h280/hp-pavilion-15-eh114.webp",
        "productName": "HP Pavilion 15-eh1147AU Laptop (AMD Ryzen 7 5700U/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4.7",
        "specScore": "63",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Radeon Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqd1GHXACT8SpIshrhArnrysuhyihDRPwzSf-SH5h-hrhhaFhrhrhhacBrWahrhrBi5r4yPF8UYhrFB5WCBox8rxQsrR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5CETlCe7-w280-h280/acer-aspire-lite-15.webp",
        "productName": "Acer Aspire Lite 15 AL15-52 Laptop (12th Gen Core i3/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹35,990",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFxnD3FOOmbUSuXhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh8bHiiXgHAobPP6hmBYihkwkp7JVxo_VZeo1HbhrhhaFhrhrhhacBrWahrhrBi54CZFlPtuhrFB51_4POO3ywja."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihhitjqGJ-w280-h280/hp-omen-16-xf0081ax.webp",
        "productName": "HP Omen 16-xf0081AX Gaming Laptop (AMD Ryzen 7 7840HS/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,35,999",
        "rating": "4.35",
        "specScore": "83",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1440 x 2560 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520Omen%252016-xf0081AX%2520Gaming%2520Laptop%2520(AMD%2520Ryzen%25207%25207840HS%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ig0i03yQn-w280-h280/infinix-inbook-y4-ma.webp",
        "productName": "Infinix INBook Y4 Max Series Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹42,990",
        "rating": "4.65",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYGf04XEHiJ251uhrhAgTYBOr3Uh7YugYuYDcIHcnrDcFa3YaFcYuUaTcAs3acY4c5ZUtcWauc5ZZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacITb5ZcUtYucTYWtUcTrBUshDhDh8ioXGZZllZAG5ZhmBYihkwkp7JJRvejxpJvZJhrhhaFhrhrhhacBrWahrhrBi5BBsnDsOlhrFB5nVZ6FjG8OnkX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iX58tvfLc-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QYIN Laptop (AMD Ryzen 7 7735HS / 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹70,990",
        "rating": "4.75",
        "specScore": "69",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF64k4AAeT40_WkhrhAgTYBOr3Uh7Taus2scYiarBricWrnhNcrnic3IyaucGcsAUrcAs3acGGZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54r3tGcTrBUshDhDh86GHGro5HHZX55hmBYihkwkp7EjbSl~SoKHx-hrhhaFhrhrhhacBrWahrhrBi5Xn2yUHrthrFB5DBbIVilxSoWp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iN66EVQTK-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83ER008GIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹53,990",
        "rating": "4.5",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF~gKUA6q8G0SyJhrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54YrtXcUtYucTYWtUcTrBUshDhDh85GbXAoiiaGPAohmBYihkwkp7_o_ES_vv1z7lhrhhaFhrhrhhacBrWahrhrBi5AX4CD4PNhrFB5se3FDoN.j9EC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC7yONe0k-w280-h280/acer-nitro-v-15-anv1.webp",
        "productName": "Acer Nitro V 15 ANV15-51 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹69,990",
        "rating": "4.15",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 SDRAM RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PbF89NA3etZiG6hrhArnrysuhyihDRPw~15zo0Jh-hrhhaFhrhrhhacBrWahrhrBi5XWZHYnoThrFB5xsq81RmmIv4C"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8W8XsfUp-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83ER008DIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹51,990",
        "rating": "4.4",
        "specScore": "55",
        "features": [
            "12th Gen intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel IrisXe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmXiUvEfUQqAvqhrhArnrysuhyihDRPwd0S55H0h-hrhhaFhrhrhhacBrWahrhrBi5bBDtZnQThrFB5NS3CHVz.3o5."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUVmH76zG-w280-h280/lenovo-yoga-slim-6-1.webp",
        "productName": "Lenovo Yoga Slim 6 14IRH8 83E00012INLaptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹81,990",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOj~pXe6nSrT06uhrhAgTYBOr3Uh7Taus2scIsWrcFTYncbc8CDWrcsTaicYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXZaPPP5oYucUtYucTYWtUcTrBUshDhDh8HHo4GlioXX5XAhmBYihkwkp70Vpb.HEbJp.7hrhhaFhrhrhhacBrWahrhrBi5bHA6lgYbhrFB55tUJoArUf_ao"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijg5vAqpe-w280-h280/xiaomi-redmi-book-14.webp",
        "productName": "Xiaomi Redmi Book 14 2024 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹49,990",
        "rating": "4",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel ARC Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520Book%252014%25202024%2520Laptop%2520(13th%2520Gen%2520Core%2520i5%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win%252011)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRWiA1gtO-w280-h280/apple-macbook-pro-14.webp",
        "productName": "Apple MacBook Pro 14 2023 Laptop (Apple M3 Pro/ 18GB/ 512GB SSD/ macOS)",
        "price": "₹1,86,899",
        "rating": "4.75",
        "specScore": "54",
        "features": [
            "Apple M3 Pro",
            "11 Cores (5P + 6E)",
            "18 GB  RAM",
            "512 GB SSD",
            "14 Core GPU",
            "14.2 inches, 3024 x 1964 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_O.DqXtlErdflQ8hrhArnrysuhyihDRPwp4ev_1Xh-hrhhaFhrhrhhacBrWahrhrBi5boXD8CP5hrFB50.Nwf1__R5q9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJ5nQp28U-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 5 5500U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹38,999",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqwJIjuV5oOq5OxhrhArnrysuhyihDRPKG..RR71h-hrhhaFhrhrhhacBrWahrhrBi5lQQasiaNhrFB5dt1JE7ynAXR9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuWVVgZly-w280-h280/gigabyte-g5-mf-e2in3.webp",
        "productName": "Gigabyte G5 MF-E2IN313SH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹81,580",
        "rating": "4.15",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI.XT.g9OkG4QeGhrhArnrysuhyihDRPw-z0mp0lh-hrhhaFhrhrhhacBrWahrhrBi5P5FrTPPUhrFB5UomAZmbj5xtl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4BkJrb0a-w280-h280/dell-g15-5530-15-202.webp",
        "productName": "Dell G15-5530 15 2023 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,00,090",
        "rating": "4.55",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9Bseb4Dz.0dI63v0hrhArnrysuhyihDRPwKR15dXRh-hrhhaFhrhrhhacBrWahrhrBi5TGPiAylOhrFB5i-jHsOd6V7IU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iceW5GKNB-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XE007DIN Laptop (AMD Ryzen 5 7530U/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹59,190",
        "rating": "4.55",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqkEbgg6j2.US3uhrhArnrysuhyihDRPwSpl5e-Zh-hrhhaFhrhrhhacBrWahrhrBi5lGgOiUQohrFB5j_jqfEFi5XAN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0UU0KgoJ-w280-h280/acer-chromebook-cb31.webp",
        "productName": "Acer Chromebook CB314-3H NX.K04SI.008 Laptop (Intel Celeron N4500/ 8GB/ 64GB SSD/ Chrome OS)",
        "price": "₹15,990",
        "rating": "4.75",
        "specScore": "34",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "64 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1080 x 1920 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzzz~21zDoboSGOhrhAgTYBOr3Uh7rAa3cAt3sna6ssOcoPoHcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6cbHcW6cannAcFUs3rWacAt3snacsFcA6Z5HcZtcAs6ycTrBUshDhDh8ggXXGPXg4PorGhmBYihkwkp7e0Z7.fEK7bd1hrhhaFhrhrhhacBrWahrhrBi5gNlF6Wi2hrFB5ofAAr6mq8OVX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJPuY9c1a-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-58GM 2023 Gaming Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graphics)",
        "price": "₹51,369",
        "rating": "4.35",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgjqWUWW4q7sRxhrhArnrysuhyihDRPwSl0d4VRh-hrhhaFhrhrhhacBrWahrhrBi5HI5l5UlUhrFB5GFdYxq_vWOX8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iioEryFQ2-w280-h280/lenovo-yoga-6-13abr8.webp",
        "productName": "Lenovo Yoga 6 13ABR8 83B2007UIN Laptop (AMD Ryzen 7 7730U/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹86,690",
        "rating": "4.05",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB LPDDR4X RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "13.3 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrElZ6QndPToKa_ahrhAgTYBOr3Uh7Taus2scIsWrcbcrnic3IyaucGcsAUrcAs3acGGZPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5Zr63Xcoc5cTrBUshDhDh8Pr4ior54lZXaXhmBYihkwkp7e0xqeo_ef~ffhrhhaFhrhrhhacBrWahrhrBi5AlFGisPyhrFB5OS0Pb-rSZHmN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iI7g7jG1u-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 2024 FA507UV-LP136WS Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,24,500",
        "rating": "4.65",
        "specScore": "77",
        "features": [
            "8th Gen AMD Ryzen 7 8845HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_HGQ6Ib83f9mKmShrhArnrysuhyihDRPX-z71~Goh-hrhhaFhrhrhhacBrWahrhrBi5CGGXbPrahrFB5EOqSgZSP55l-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTH3wkImb-w280-h280/infinix-gt-book-gl61.webp",
        "productName": "Infinix GT Book GL613 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11 Home/ 6GB RTX 4050 Graphics)",
        "price": "₹79,990",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYekBzXJJSe2Ju_hrhAgTYBOr3Uh7YugYuYDcWUcFa3YaFcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4PclPc8cWTb5ZcrAAaFFs3YaFc6sDcWrnhNcTrBUshDhDh8GigAAaZ6g544bhmBYihkwkpSfeHH71~z70SXhrhhaFhrhrhhacBrWahrhrBi5b2AnuFaghrFB5rTTgOypOTro-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJPiJkDaT-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 11 Laptop (Snapdragon X Elite/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,61,990",
        "rating": "4.65",
        "specScore": "51",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uIPzetyUnDlnFw-5hrhAA3snrh7nYA3sFsgUcFC3grAacB3sc55UtcaiYUh3c8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtc5bW6c3rnc45oW6c3snchnch-hDZPX4obhrhhaFhrhrhhacBrWahrhrBi5rAN8UI6OhrFB5rtjR~9lCEjHN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQEPLT1pd-w280-h280/lenovo-loq-83gs000pi.webp",
        "productName": "Lenovo LOQ 83GS000PIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹70,980",
        "rating": "4",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwNtTDSKGVWaR4GhrhArnrysuhyihDRPKH5wz4Jbh-hrhhaFhrhrhhacBrWahrhrBi5TGQDbr2ThrFB5bkuF7jToBKaG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icJEZzZeo-w280-h280/acer-al15g-52-2024-g.webp",
        "productName": "Acer ‎AL15G- 52 2024 Gaming Laptop (12th Gen Core i5-12450H/ 16GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹51,990",
        "rating": "4.15",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1ToqX8tkoSnIEhrhAgTYBOr3Uh7rAa3crTWcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrT54Wc4ocWrnhNcTrBUshDhDh8ZAbb4455abriZhmBYihkwkpSoz1ejX0KoH0-hrhhaFhrhrhhacBrWahrhrBi5aPiUDyPghrFB5~zx4pBPn.-HP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inO4sAHoL-w280-h280/msi-thin-15-b12uc-16.webp",
        "productName": "MSI Thin 15 B12UC-1691IN Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX3050 Graph)",
        "price": "₹66,990",
        "rating": "4.7",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqz9VCOd~3dkN1ihrhArnrysuhyihDRPw0l-5~e-h-hrhhaFhrhrhhacBrWahrhrBi5siIgtNYghrFB5EtRApuVS9RRe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioI55TxRl-w280-h280/msi-cyborg-15-a12udx.webp",
        "productName": "MSI Cyborg 15 A12UDX-1049IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹62,990",
        "rating": "4.4",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIdDKIoUZ2dwFG~hrhArnrysuhyihDRPw_KS55o~h-hrhhaFhrhrhhacBrWahrhrBi5W4ADolbIhrFB5y.G6YFURISFQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixAdr32h3-w280-h280/hp-victus-15-fa0444t.webp",
        "productName": "HP Victus 15-fa0444TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB RTX 3050)",
        "price": "₹66,990",
        "rating": "4.7",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYmlVG-9RFuRJgShrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55cB3scHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgrPHHHUDcWrnhNcTrBUshDhDh8lgAX5o5aHGl44hmBYihkwkpSfXV0_-p4S.7whrhhaFhrhrhhacBrWahrhrBi52Xa6OXN8hrFB5G9w2ojR6KNbT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYSzjXnIo-w280-h280/dell-inspiron-3530-o.webp",
        "productName": "Dell Inspiron 3530 OIN353034071RINS1M Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹57,350",
        "rating": "4.05",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67ZkixRPK--2nYfhrhArnrysuhyihDRPKof5RmKzh-hrhhaFhrhrhhacBrWahrhrBi53aOI88r8hrFB5yHAK5_eJ.oS5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7FWQT7zR-w280-h280/asus-rog-strix-g16-g.webp",
        "productName": "Asus ROG Strix G16 G614JV-N3474WS Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,39,990",
        "rating": "4.5",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9XGetmbkYyu3BCCfhrhArnrysuhyihDRPlzRHx1VJh-hrhhaFhrhrhhacBrWahrhrBi5n5lnO6UghrFB5SXBrIQ63p-m4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iL1KCQesF-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-73 NX.KSGSI.001 Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹1,09,990",
        "rating": "4.6",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 5 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated Arc Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB7_2~.B36fqndf8hrhArnrysuhyihDRPKwbK0Z5lh-hrhhaFhrhrhhacBrWahrhrBi5nWyNQXyGhrFB5t1XYU1N~YE.B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQwrLzbyJ-w280-h280/asus-vivobook-16-x16.webp",
        "productName": "Asus Vivobook 16 X1605ZAC-MB742WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹60,990",
        "rating": "4.15",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQIRs60SzpeVxF3hrhAgTYBOr3Uh7rFCFcYuUaTcAs3acYGc5oUtcWauc5oGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacD5bP4yrAcn6GHo8FcTrBUshDhDh8g5ibZ5goi6Xo4hmBYihkwkpSff.d_4fx.01-hrhhaFhrhrhhacBrWahrhrBi5OuCloGFAhrFB5gb~2VarJ9tX0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itdOWu3UC-w280-h280/asus-vivobook-16-x16.webp",
        "productName": "Asus Vivobook 16 X1605ZAC-MB540WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹54,990",
        "rating": "4.4",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbRSXToiFY3EDUjjjuD_hrhAgTYBOr3Uh7rFCFcYuUaTcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacD5bP4yrAcn64HP8FcUtYucTYWtUcTrBUshDhDh8GGiooHH6GAAoXhmBYihkwkpSf7X.bxSxz0.fhrhhaFhrhrhhacBrWahrhrBi5WAs5HZrbhrFB5-FG6rv5RyB_C"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikIKwQDxm-w280-h280/dell-inspiron-7440-l.webp",
        "productName": "Dell Inspiron 7440 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹97,590",
        "rating": "4.75",
        "specScore": "63",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphic",
            "14 inches, 2240 x 1400 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqTSemzwzTsaPS0hrhArnrysuhyihDRPwfm_.oXxh-hrhhaFhrhrhhacBrWahrhrBi5PoUTtH3XhrFB5R8Vv_9WP7IRK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwect8CnH-w280-h280/lenovo-legion-5-16ir.webp",
        "productName": "Lenovo Legion 5 16IRX9 83DG004SIN Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB RTX4060)",
        "price": "₹1,44,990",
        "rating": "4.55",
        "specScore": "77",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_bi5xXYJ22QNU3nhrhArnrysuhyihDRPw_XJ.fwZh-hrhhaFhrhrhhacBrWahrhrBi53sF6soG4hrFB5S9Ie6.4D6B41"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXObWCRDP-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JFA02PIN Laptop (AMD Ryzen 3 7330U/ 8GB/ 512 GB SSD/ Win11)",
        "price": "₹30,540",
        "rating": "4.6",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 3 7330U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzAB2IP.mjN6fCwhrhAgTYBOr3Uh7Taus2scrnic3IyaucZcNCricAs3acGZZPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacUtYuO6ssOc54cW4cUtYucTYWtUcTrBUshDhDh85bHaAXa4666Z4hmBYihkwkp7f7oZSZwvjREzhrhhaFhrhrhhacBrWahrhrBi5OGZo4PDNhrFB5eXkwIPtfk3Em"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4pngyiNB-w280-h280/lenovo-thinkbook-16.webp",
        "productName": "Lenovo ThinkBook 16 G6 21KHA0J6IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹57,490",
        "rating": "4.2",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Iris Xe Graphics",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqdWkDBXe8~0ZCphrhArnrysuhyihDRPw.GRx~.mh-hrhhaFhrhrhhacBrWahrhrBi5r6ba4olrhrFB5k3o4Tzvv_.kS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibgcLPSg5-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS003QIN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹66,490",
        "rating": "4.6",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0H5b9U-Cpqu66zrhrhAA3snrh7Taus2scTsNc54YrDlcYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacZb4cTCurcW3aIcocZXcOWch-hDZP4bXohrhhaFhrhrhhacBrWahrhrBi5BtiWaiU5hrFB5UOrgz0w4Evg."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iX9CLGY1Z-w280-h280/acer-nitro-v-anv15-5.webp",
        "productName": "Acer Nitro V ANV15-51 Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050)",
        "price": "₹84,990",
        "rating": "4.1",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqajr8EK2ekPNA5hrhArnrysuhyihDRPwe-vdZ1-h-hrhhaFhrhrhhacBrWahrhrBi5u3uHHBYDhrFB5HkCz3D-kP-_8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaxcihevC-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios 16 ‎PH16-72 NH.QNZSI.002 Gaming Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11/ 12GB Graph)",
        "price": "₹2,49,990",
        "rating": "4.6",
        "specScore": "87",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_djPb58g--TSTPshrhArnrysuhyihDRPKoKlZSfoh-hrhhaFhrhrhhacBrWahrhrBi5UF4UbTDrhrFB5eJUWSapv~XHg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-io36GPCrk-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 ‎PHN16-72 Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,74,990",
        "rating": "4.05",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BD_ulgSkVw7GJVEhrhArnrysuhyihDRPw_1JGRv.h-hrhhaFhrhrhhacBrWahrhrBi5nAoWtygBhrFB5sSbyGUxe~NKe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEfg1pmtV-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 3 5300U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹29,990",
        "rating": "4.25",
        "specScore": "55",
        "features": [
            "5th Gen AMD Ryzen 3 5300U",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFRYGpq--pQ1_KEhrhAgTYBOr3Uh7rAa3crnic3IyaucZcNCricAs3ac4ZPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54cH5cUtYucTYWtUcTrBUshDhDh8i5GbHoib6GZrZhmBYihkwkpSoXEHJKxREV1ZhrhhaFhrhrhhacBrWahrhrBi5tBoFX3HChrFB5BCUjQfdp4f8E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iU8yRXcpy-w280-h280/hp-envy-x360-14-fc00.webp",
        "productName": "HP Envy x360 14-fc0078TU Laptop (Intel Core Ultra 5 125U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,01,990",
        "rating": "4.45",
        "specScore": "64",
        "features": [
            "1st Gen Intel Core Ultra 5 125U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated Intel Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uDUZy9lma2KyZg2QhrhAA3snrh7tBcau2IcDZbPc5HcgAPPGXUCcYuUaTcAs3acCTU3rc4cUsCAtFA3aaucocYuc5cTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcsTaiciYFBTrIcnFcsggYAacoPo5crUnsFBta3YAc6TCac5cZlcOWch-hDZP4XHPhrhhaFhrhrhhacBrWahrhrBi5uZ6srTHXhrFB5zd7V1-JR8SQx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTtC1E9Z6-w280-h280/hp-victus-15-fa1128t.webp",
        "productName": "HP Victus 15-fa1128TX Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹61,990",
        "rating": "4.55",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GVJOi2y_KI_dZVhrhAA3snrh7tBc2YAUCFcYuUaTcAs3acY4c5ZUtcWaucWrnhNcTrBUsBc5bW6c45oU6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcoP4PcBa3gs3nruAac6TCacocolcOWch-hDZPbHHXhrhhaFhrhrhhacBrWahrhrBi5Za2FCUBBhrFB5CAb5AnIz6d4Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEFytCIeV-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2024 MXCT3HN/A Laptop (Apple M3/ 16GB/ 512GB SSD/ MacOS)",
        "price": "₹1,47,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "16 GB  RAM",
            "512 GB SSD",
            "Apple 10 Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BCGQGS5itX_-_PehrhArnrysuhyihDRPw_oZxe~mh-hrhhaFhrhrhhacBrWahrhrBi5NQaFHHP4hrFB5VNniw2RuzN6."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioyzKxmaJ-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83EM0023IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹61,400",
        "rating": "4.25",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzCCFX9.P106ZnphrhAgTYBOr3Uh7Taus2scYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXZanPPoZYucTrBUshDhDh8gGiboG64XAbZghmBYihkwkp7f-7EEES-fS.qhrhhaFhrhrhhacBrWahrhrBi54BO3i4YThrFB5yYNRqFS86gdb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icbt8fGxV-w280-h280/msi-thin-a15-ai-b7ve.webp",
        "productName": "MSI Thin A15 AI B7VE-066IN Gaming Laptop (AMD Ryzen 5 7535H/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹71,990",
        "rating": "4.5",
        "specScore": "71",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqJ24ray6oBHGaahrhArnrysuhyihDRPw04x7K_ph-hrhhaFhrhrhhacBrWahrhrBi5Z5PDNuXWhrFB5HOR5.01KYxUe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2ZY1egVH-w280-h280/msi-thin-a15-ai-b7ve.webp",
        "productName": "MSI Thin A15 AI B7VE-065IN Gaming Laptop (AMD Ryzen 7 7735H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹79,990",
        "rating": "4.25",
        "specScore": "73",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqr_N7.6T7ZXN_UhrhArnrysuhyihDRPw04K_5_fh-hrhhaFhrhrhhacBrWahrhrBi5syI523CuhrFB59NCRN6txfJjD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijyZ0xixM-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 83DA0049IN Laptop (Intel Core Ultra 5/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹87,000",
        "rating": "4.45",
        "specScore": "48",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrElSqUbTUG6IKrbhrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4crYcBAc8CDWrcsTaicYuUaTcAs3acCTU3rc5o4tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5HYntlcTrBUshDhDh8PXlPZ5GoZrXighmBYihkwkp7_jElRG777.SHhrhhaFhrhrhhacBrWahrhrBi5AIbN4grHhrFB5m5EA7T7S79p0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6JpW7cFK-w280-h280/hp-14s-dq5138tu-lapt.webp",
        "productName": "HP 14s-dq5138tu Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.75",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G4Gf7uFVF_B3TnhrhAA3snrh7tBc5HFciN45ZXUCcYuUaTcAs3acYZc5oUtcWaucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5curUCrTcFYThCc5cHbcOWch-hDZPHHbHhrhhaFhrhrhhacBrWahrhrBi5YAWFtlQ5hrFB5JIpVtVSRB5ek"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0qPbIdq9-w280-h280/hp-pavilion-15-eh114.webp",
        "productName": "HP Pavilion 15-eh1147AU Laptop (AMD Ryzen 7 5700U/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4.7",
        "specScore": "63",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Radeon Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqd1GHXACT8SpIshrhArnrysuhyihDRPwzSf-SH5h-hrhhaFhrhrhhacBrWahrhrBi5r4yPF8UYhrFB5WCBox8rxQsrR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iryqqjT7R-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 14IMH9 83DA0043IN Laptop (Intel Core Ultra 5/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹76,990",
        "rating": "4.35",
        "specScore": "55",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HGjVgIIrCUC1g7hrhAA3snrh7Taus2scYiarBricFTYnc4c5HYntlcYuUaTcAs3acCTU3rc4cTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnac5HcYuAtcsTaiciYFBTrIcnFcsggYAacoPo5cATsCicW3aIc5cHbcOWch-hDZPHH45hrhhaFhrhrhhacBrWahrhrBi5ITgo5CaBhrFB5_m60Vg9-b8d2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5CETlCe7-w280-h280/acer-aspire-lite-15.webp",
        "productName": "Acer Aspire Lite 15 AL15-52 Laptop (12th Gen Core i3/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹35,990",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFxnD3FOOmbUSuXhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh8bHiiXgHAobPP6hmBYihkwkp7JVxo_VZeo1HbhrhhaFhrhrhhacBrWahrhrBi54CZFlPtuhrFB51_4POO3ywja."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihhitjqGJ-w280-h280/hp-omen-16-xf0081ax.webp",
        "productName": "HP Omen 16-xf0081AX Gaming Laptop (AMD Ryzen 7 7840HS/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,35,999",
        "rating": "4.35",
        "specScore": "83",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1440 x 2560 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520Omen%252016-xf0081AX%2520Gaming%2520Laptop%2520(AMD%2520Ryzen%25207%25207840HS%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYtPeX1iM-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00M6IN Laptop (AMD Ryzen 5 7535HS / 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹62,990",
        "rating": "4.3",
        "specScore": "68",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFJbmCEJEqAs94YhrhAgTYBOr3Uh7Taus2scYiarBricWrnhNcrnic3Iyauc4ctaDrcAs3acG4Z4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54r3tGcTrBUshDhDh8Xi6aAalogZH5PhmBYihkwkp7EjbS0f7-.l_phrhhaFhrhrhhacBrWahrhrBi5NYysWZDIhrFB55GWenq7fVs.Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iN66EVQTK-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83ER008GIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹53,400",
        "rating": "4.5",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmNJ3YnafaFlbkhrhArnrysuhyihDRPwvX_fbp7h-hrhhaFhrhrhhacBrWahrhrBi5AX4CD4PNhrFB5GbOZ0Z.1IbwC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isMqbVbno-w280-h280/acer-nitro-v16-anv16.webp",
        "productName": "Acer Nitro V16 ANV16-41 Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 1TB SSD/ Win11/ 8GB Graphics)",
        "price": "₹1,09,990",
        "rating": "4.5",
        "specScore": "69",
        "features": [
            "8th Gen AMD Ryzen 7 8845HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGvDr.tUmvX4Rix6hrhAgTYBOr3Uh7rAa3crnic3IyaucGcsAUrcAs3acXXH4tFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPcru25bcH5cWrnhNcTrBUshDhDh85gZaXiG6ZrbgXhmBYihkwkpSoXEHvZSp_xfvhrhhaFhrhrhhacBrWahrhrBi558H3QnOrhrFB5zP6~vniCXQ6S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUVmH76zG-w280-h280/lenovo-yoga-slim-6-1.webp",
        "productName": "Lenovo Yoga Slim 6 14IRH8 83E00012INLaptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹81,990",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOj~pXe6nSrT06uhrhAgTYBOr3Uh7Taus2scIsWrcFTYncbc8CDWrcsTaicYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXZaPPP5oYucUtYucTYWtUcTrBUshDhDh8HHo4GlioXX5XAhmBYihkwkp70Vpb.HEbJp.7hrhhaFhrhrhhacBrWahrhrBi5bHA6lgYbhrFB55tUJoArUf_ao"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irZTgedXS-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 Gen 6 82K2028QIN Laptop (AMD Ryzen 5 5500H/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹47,990",
        "rating": "4.4",
        "specScore": "62",
        "features": [
            "5th Gen AMD Ryzen 5 5500H",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrznZ9XYkouBP5DChrhAgTYBOr3Uh7Taus2scrnic3Iyauc4cNCricAs3ac34c44PPtcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcu2YiYrcWags3Aac3UDcoP4PcXoOoPoXNYucWrnhNcTrBUshDhDh8rZPHXaPibl54rhmBYihkwkp7EqxVe_1RpSE.hrhhaFhrhrhhacBrWahrhrBi5UTnT5ONGhrFB5BP6v5rRdDETv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAAsGnkgW-w280-h280/hp-victus-15-fa1134t.webp",
        "productName": "HP Victus 15-fa1134TX Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹88,490",
        "rating": "4.35",
        "specScore": "73",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrElUz~BUg7EFQV9hrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc54cgr55ZHUDcWrnhNcTrBUshDhDh8ZPXHGZ4HoP4AXhmBYihkwkp7zzGq7ewwzE-zhrhhaFhrhrhhacBrWahrhrBi5PPlasg4AhrFB5D8jNAyDNGPPP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJ5nQp28U-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 5 5500U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹37,990",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF7tl_p1SUwbnsjhrhAgTYBOr3Uh7rAa3crFBY3acThscrnic3Iyauc4ctaDrcAs3ac44PPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrT54cH5cUtYucTYWtUcTrBUshDhDh8Pi4aiigGiPi4ohmBYihkwkp7EoKl.j_wjSREhrhhaFhrhrhhacBrWahrhrBi5lQQasiaNhrFB5WP57f-6_DUnn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i68Na06Rc-w280-h280/asus-vivobook-go-14.webp",
        "productName": "Asus Vivobook Go 14 E1404FA-NK547WS Laptop (Ryzen 5 7520U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹39,990",
        "rating": "4.05",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFS6mwNZBvSVSBwhrhAgTYBOr3Uh7rFCFc2Y2s6ssOc5Hcrnic3Iyauc4cNCricAs3acG4oPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnaca5HPHgrcuO4HG8FcUtYucTYWtUcTrBUshDhDh8GZbilAaloA5l6hmBYihkwkp7eoj-lvqj4..KhrhhaFhrhrhhacBrWahrhrBi5ZibPA2TPhrFB5AvsVjk1n_stI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4BkJrb0a-w280-h280/dell-g15-5530-15-202.webp",
        "productName": "Dell G15-5530 15 2023 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,00,090",
        "rating": "4.55",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9Bseb4Dz.0dI63v0hrhArnrysuhyihDRPwKR15dXRh-hrhhaFhrhrhhacBrWahrhrBi5TGPiAylOhrFB5i-jHsOd6V7IU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYpFFSvWh-w280-h280/asus-vivobook-16x-k3.webp",
        "productName": "Asus Vivobook 16X K3605ZU-MB542WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹79,990",
        "rating": "4.4",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA Geforce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI_5baB~z1VR0OAhrhArnrysuhyihDRPwfzRm4ZSh-hrhhaFhrhrhhacBrWahrhrBi54lZ6stX4hrFB54AP~1uT_Nyxg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijiM4NgfF-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 82SB00V5IN Laptop (AMD Ryzen 7 6800H/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹64,990",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "6th Gen AMD Ryzen 7 6800H",
            "Octa Core, 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIk31iJ_6ze~dXehrhArnrysuhyihDRPw704-veVh-hrhhaFhrhrhhacBrWahrhrBi5lNgNaraYhrFB50T6B.HnoXx9B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iS8k362za-w280-h280/primebook-pbmtwifi11.webp",
        "productName": "Primebook PBMTWIFI11064 Wi-Fi Laptop (MediaTek MT8183/ 4GB/ 64B eMMC/ Prime OS)",
        "price": "₹10,990",
        "rating": "4.25",
        "specScore": "30",
        "features": [
            "MediaTek MT8183",
            "Octa Core",
            "4 GB LPDDR4 RAM",
            "64 GB Hard Disk",
            "ARM Mali G72",
            "11.6 inches, 1366 x 768 pixels",
            "1 Year Warranty",
            "2 USB 3.0 Ports"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtsIi3B.I3uD7.ihrhAgTYBOr3Uh7B3Yna6ssOcnaiYrUaOcnUX5XZcHcW6cbHcW6cannAcFUs3rWachY3sYic55c8YgYcUtYucTYWtUcTrBUshDhDh8A5bHPlrbi6ZiPhmBYihkwkpSff.dZxfRJzeVhrhhaFhrhrhhacBrWahrhrBi5T6niiGb3hrFB5XXU3ozjuyXNW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJxqfq0T8-w280-h280/hp-pavilion-plus-14.webp",
        "productName": "HP Pavilion Plus ‎14-ey0789AU Laptop (AMD Ryzen 7 7840H/ 16GB/ 1TB SSD/ Win 11)",
        "price": "₹84,990",
        "rating": "4.1",
        "specScore": "69",
        "features": [
            "7th Gen Amd Ryzen 7 7840H",
            "Octa Core, 16 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "AMD Radeon 780M Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEXxC52C9TFBnFwhrhAgTYBOr3Uh7tBcBr2YTh3cBTCFcrYcBs8ahBcTrBUsBcrnic3IyaucGcsAUrcAs3acGXHPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5HcaIPGXlrCh-hDh8riigbaH6AgaG4hmBYihkwkp7EwqfJZ71exoehrhhaFhrhrhhacBrWahrhrBi5ZAltoiPlhrFB5_VdXBEywK2ST"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iR2qfTOwc-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JFA00BIN Laptop (AMD Ryzen 7 7730U/ 8 GB/ 512 GB SSD/ Win11)",
        "price": "₹44,990",
        "rating": "4.4",
        "specScore": "65",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq76tfZK3jwmNRRhrhArnrysuhyihDRPw7wvvw5.h-hrhhaFhrhrhhacBrWahrhrBi5g6AN2UbnhrFB576isUN~G8nPV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iCKZmVAt5-w280-h280/asus-vivobook-16-202.webp",
        "productName": "Asus Vivobook 16 2023 X1605VA-MB947WS Laptop (13th Gen Core i9/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹94,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKH9T9z5_15XQxohrhArnrysuhyihDRPwSp.vwXlh-hrhhaFhrhrhhacBrWahrhrBi5syaaGUF3hrFB5qIeHysnyadbs"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYVjaL6Vi-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 82K101PCIN Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹49,499",
        "rating": "4.5",
        "specScore": "63",
        "features": [
            "11th Gen Intel Core i5 11320H",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwA8~~eiRl3.xPBhrhArnrysuhyihDRPw70ZR1Vbh-hrhhaFhrhrhhacBrWahrhrBi52IsN4ONbhrFB5sF2pIdIHKH1Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJPuY9c1a-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-58GM 2023 Gaming Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graphics)",
        "price": "₹51,369",
        "rating": "4.35",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgjqWUWW4q7sRxhrhArnrysuhyihDRPwSl0d4VRh-hrhhaFhrhrhhacBrWahrhrBi5HI5l5UlUhrFB5GFdYxq_vWOX8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4Cu6Pyzw-w280-h280/chuwi-freebook-lapto.webp",
        "productName": "Chuwi FreeBook Laptop (12th Gen Core i3/ 12GB/ 512GB SSD/ Win11)",
        "price": "₹37,990",
        "rating": "4.2",
        "specScore": "44",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "12 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Intel UHD Graphics",
            "13.5 inches, 2256 x 1504 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqwHTwaDlkUZA7ChrhArnrysuhyihDRPR5pb_-R-h-hrhhaFhrhrhhacBrWahrhrBi5DFNUFaUihrFB5DOOkj4tC.z9."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inlDeQxuf-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HE-HN385WS Gaming Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹84,990",
        "rating": "4.25",
        "specScore": "71",
        "features": [
            "11th Gen Intel Core i7 11800H",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050 Ti",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEXxC52C9TFBnFwhrhAgTYBOr3Uh7rFCFcUCgcWrnhNcg54cYuUaTcAs3acYGc55UtcWauc55XPPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHW6cu2YiYrcZP4PcUYc5HHctycgD4PbtactuZX48FcTrBUshDhDh8PoHHG4aGioHiZhmBYihkwkp7zEVR.GG1~17dhrhhaFhrhrhhacBrWahrhrBi5TylCNiQPhrFB5xIdOm8amVFbi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieBtL3oIs-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ993WS Laptop (12th Gen Core i3/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹37,299",
        "rating": "4.7",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqRBO~rZXAJgu~dhrhArnrysuhyihDRPKbJSwf4Vh-hrhhaFhrhrhhacBrWahrhrBi5rPi38UyGhrFB5lHjKXwFIuwNz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iV4zF3lFZ-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2023 K3605ZC-MBN752WS Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹82,990",
        "rating": "4.65",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY0Gkz.EX2Yr5NihrhAgTYBOr3Uh7rFCFc2Y2s6ssOc5bDcoPoZcA3arUs3cYuUaTctcFa3YaFcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcbPctyc4PcUWBcOZbP4yAcn6uG4o8FcWrnhNcTrBUshDhDh8agrl66PGgZHZAhmBYihkwkp71d7HS__071jehrhhaFhrhrhhacBrWahrhrBi5ZBIIBNHXhrFB5aT0EW35p3JB0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqCyydPko-w280-h280/asus-vivobook-16-202.webp",
        "productName": "Asus Vivobook 16 2023 X1605ZAB-MB322WS Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹35,990",
        "rating": "4.4",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw01JofmtYUoFywhrhArnrysuhyihDRPwx0fe.x7h-hrhhaFhrhrhhacBrWahrhrBi5sO5bPna6hrFB5dP~x4tIdvW0n"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHvI6zlO3-w280-h280/hp-250-g9-7m659pa-la.webp",
        "productName": "HP 250 G9 7M659PA Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,000",
        "rating": "4.5",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIG9USk0bo.kVR4hrhArnrysuhyihDRPw4pxpSG4h-hrhhaFhrhrhhacBrWahrhrBi5gBNF6IsQhrFB5wQY81NUHX63T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipiGdLesZ-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 16IAH8 83BG000PIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹56,990",
        "rating": "4.6",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67ZjjfT.sCOSVH6hrhArnrysuhyihDRPwxxHov-bh-hrhhaFhrhrhhacBrWahrhrBi5usl8Tin3hrFB5yf2nPPYGkb6Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSw4k0zMb-w280-h280/hp-victus-15-fa0187t.webp",
        "productName": "HP Victus 15-fa0187TX Gaming Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹87,500",
        "rating": "4.6",
        "specScore": "71",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PS6ZA6jNW3dqd9hrhArnrysuhyihDRPwvbpZv-4h-hrhhaFhrhrhhacBrWahrhrBi5soQD3InZhrFB59F-1EHWup7ft"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipGZa1Y51-w280-h280/asus-vivobook-go-14.webp",
        "productName": "Asus Vivobook Go 14 2023 E1404FA-NK327WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹32,990",
        "rating": "4.7",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrziU6G10j3HoJsAhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc5Hcrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca5HPHgrcuOZoG8FcUtYucTYWtUcTrBUshDhDh8ibGZZgGZZoGG5hmBYihkwkp7eoj-ZqxvevR~hrhhaFhrhrhhacBrWahrhrBi5GFtulCtXhrFB5mRv9KV_buyH."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZi43LFHR-w280-h280/hp-pavilion-15-eg301.webp",
        "productName": "HP Pavilion 15-eg3017TU Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹68,999",
        "rating": "4.7",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HoR1ix~K7xTeO~hrhAA3snrh7tBcBr2YTh3c54caWZP5GUCcYuUaTcAs3acY4c5ZUtcWauc54cbcYuAtc5bW6c5U6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcY3YFcDacgCTTcticYBFciYFBTrIcgsWc6TCacXC4WPBrch-hDoG4bGXhrhhaFhrhrhhacBrWahrhrBi5UNWAPOIUhrFB51Vu508HHGN66"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igu4JTzCs-w280-h280/hp-victus-15-fb0153a.webp",
        "productName": "HP Victus 15-fb0153AX Gaming Laptop (AMD Ryzen 5 5600H/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹50,999",
        "rating": "4.4",
        "specScore": "64",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB AMD Radeon RX 6500M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK4f~E6pPvGST8m7hrhAA3snrh7tBc2YAUCFc54cg6P54ZrDcrnic3Iyauc4c54cbcYuAtcXW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5crnic3riasuc3Dcb4PPncgticYBFciYFBTrIcBa3gs3nruAac6TCacXt4OoBrch-hDoG4GbPhrhhaFhrhrhhacBrWahrhrBi5yH5OyDZDhrFB5Z1WVKb1Rp-.u"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iboqoOzqN-w280-h280/asus-vivobook-14-202.webp",
        "productName": "Asus VivoBook 14 2023 X1404ZA-NK321WS Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹34,990",
        "rating": "4.3",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwED~wsJ~DQi39uhrhArnrysuhyihDRPww1R1feRh-hrhhaFhrhrhhacBrWahrhrBi5bZobriruhrFB50wVX~7ixea1k"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iI1E0yTwe-w280-h280/acer-predator-16-nh.webp",
        "productName": "Acer Predator 16 NH.QLUSI.005 Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,29,990",
        "rating": "4.45",
        "specScore": "74",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGE~OdaOZvn5GsothrhAgTYBOr3Uh7rAa3cBhBrUs3ctaTYsFc5bcYuUaTcAs3acYlc5ZUtcWauc5ZlPPtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPcBtu5bcG5clZlTcWrnhNcTrBUshDhDh8oG65GlaZHGg45hmBYihkwkp7v4~q0lZxbo0whrhhaFhrhrhhacBrWahrhrBi56TXXoyYWhrFB5jownjTiW4NzK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igBHFf5Rw-w280-h280/hp-pavilion-x360-14.webp",
        "productName": "HP Pavilion x360 14-ek1074TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹69,990",
        "rating": "4.55",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gkl0-N6t~-1dGehrhAA3snrh7tBcBr2YTh3c5HcaO5PGHUCcYuUaTcAs3acY4c5ZUtcWauc5HcYuAtc5bW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcCticgticYBFciYFBTrIcurUC3rTcFYThCcXA4t4Brch-hDoG4545hrhhaFhrhrhhacBrWahrhrBi5abNTbOgHhrFB53GGi2w5f-C49"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPpE8zBZh-w280-h280/lenovo-loq-15aph8-82.webp",
        "productName": "Lenovo LOQ 15APH8 82XT004HIN 2023 Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹79,938",
        "rating": "4.4",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI_PKlIVH~IyAZahrhArnrysuhyihDRPw.b1J0~_h-hrhhaFhrhrhhacBrWahrhrBi5uT5sBUiOhrFB5KQgU.DH9GVqj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipfvL0iyE-w280-h280/lenovo-loq-15aph8-82.webp",
        "productName": "Lenovo LOQ 15APH8 82XT004JIN 2023 Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,33,790",
        "rating": "4.75",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~99bDEIE9KlyfQnhrhAgTYBOr3Uh7Taus2scTsNcrYcBs8ahBcrnic3IyaucGcsAUrcAs3acGXHPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc54rBtXcWrnhNcTrBUshDhDh8o5g5lAX6l6glHhmBYihkwkp7vwlvR-dS__VfhrhhaFhrhrhhacBrWahrhrBi5CX25OuYZhrFB5sCuzGJeYKy2I"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifYyhbmGZ-w280-h280/hp-omen-16-wf0111tx.webp",
        "productName": "HP Omen 16-wf0111TX Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,28,990",
        "rating": "4.3",
        "specScore": "73",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFRQHO2.PI_Qtng_l5hrhAgTYBOr3Uh7tBcsh2cYuUaTcAs3acYGc5ZUtcWauc5ZGPPtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5bc8gP555UDcWrnhNcTrBUshDhDh84r6AoH645g5GrhmBYihkwkpSxojzVSV-.4~-hrhhaFhrhrhhacBrWahrhrBi5bNnGCDQuhrFB51A9Z7pe2Qn5a"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKed74J4n-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 21JF002CIN Laptop (AMD Ryzen 3 7330U/ 8 GB/ 512 GB SSD/ DOS)",
        "price": "₹27,990",
        "rating": "4.4",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 3 7330U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQiurZxH9Ef20PihrhAgTYBOr3Uh7Taus2scrnic3IyaucZcNCricAs3acGZZPcCcXcW6c45ocW6cFFicisFcUtYuO6ssOc54c6CFYuaFFcTrBUshDhDh85A6baogolZrgGhmBYihkwkp7vod-pdSwSJ.JhrhhaFhrhrhhacBrWahrhrBi5FYHQiia2hrFB5N4xwwRqb3pdi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUJMarAwV-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 2023 82X70033IN Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹40,500",
        "rating": "4",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i3 1305U",
            "5 Cores (1P + 4E), 6 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xCkqyQ.jsKwrpPhrhArnrysuhyihDRPwl~_KlJ.h-hrhhaFhrhrhhacBrWahrhrBi5yTT2Xit3hrFB506Xd0ZttAC9o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKn0pAdV6-w280-h280/hp-14-gr0000tu-lapto.webp",
        "productName": "HP 14-gr0000TU Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqquVK4CnH5CNlGhrhArnrysuhyihDRPwlKmGzSzh-hrhhaFhrhrhhacBrWahrhrBi5o5lBiHabhrFB52GOallEpkFWd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inG5CsCJn-w280-h280/dell-inspiron-3525-l.webp",
        "productName": "Dell Inspiron 3525 Laptop (AMD Ryzen 5 5500U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹36,990",
        "rating": "4.1",
        "specScore": "59",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqRAgp2GFiQarr0hrhArnrysuhyihDRPwd.X~d-wh-hrhhaFhrhrhhacBrWahrhrBi5HIsBsNG6hrFB5NIHTPqjWeNfa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWgANKXGb-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED 2023 S5504VA-MA554WS Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹78,990",
        "rating": "4.4",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIJ.PB46wajnGnqhrhArnrysuhyihDRPlzXpZ5pmh-hrhhaFhrhrhhacBrWahrhrBi523AZlOFNhrFB5QJiDgUqr~v1t"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i66WzFcoY-w280-h280/dell-inspiron-5630-l.webp",
        "productName": "Dell Inspiron 5630 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹68,719",
        "rating": "4.6",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 1340P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwsm2uvemA~eodQhrhArnrysuhyihDRPKRm-VKl.h-hrhhaFhrhrhhacBrWahrhrBi5ZBaBHXDshrFB5rHq_~jFu29yl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4lIeV0R6-w280-h280/lenovo-legion-5-pro.webp",
        "productName": "Lenovo Legion 5 Pro 2023 Gaming Laptop (13th Gen Core i7/ 32GB/ 1TB SSD/ Win11/ 16GB Graph)",
        "price": "₹1,72,990",
        "rating": "4.65",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DLenovo%2520Legion%25205%2520Pro%25202023%2520Gaming%2520Laptop%2520(13th%2520Gen%2520Core%2520i7%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%252F%252016GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1LBXdC3b-w280-h280/hp-pavilion-15-eg302.webp",
        "productName": "HP Pavilion 15-eg3027TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.4",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 1340p",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF_P_.IR5nY5ubOhrhAgTYBOr3Uh7tBcBr2YTh3cYuUaTcAs3acY4c5ZUtcWauc5ZHPBc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54caWZPoGUCcUtYucTYWtUcTrBUshDhDh8iPZAAXiiXA6PahmBYihkwkp71EfR.11HJqqxhrhhaFhrhrhhacBrWahrhrBi5HCuTDBDFhrFB5lDGPuvDAqS93"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLzN4mD5u-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 2023 FX507ZV-LP094W Gaming Laptop (12th Gen Core i7/ 16GB/512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,02,000",
        "rating": "4.25",
        "specScore": "74",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFRQ5aoG6Q6Ejj1zlKhrhAgTYBOr3Uh7rFCFcUCgcWrnhNcg54coPoZclP8t3c6rUhUIcYuUaTctcFa3YaFcAs3acYGc5oUtcWauc5oGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5HHctyc5HPcUWBcgD4PGy2cTBPlH8cTrBUshDhDh8Xl6b4lgr5gAZAhmBYihkwkp71x1wzR_qzfKKhrhhaFhrhrhhacBrWahrhrBi5BUT3FOIChrFB5gHkG4~BO1VPO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivnzUtff7-w280-h280/hp-15s-fr5009tu-lapt.webp",
        "productName": "HP 15s-fr5009TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹35,990",
        "rating": "4.05",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiwBmdgVWCFXOgCQvhrhAA3snrh7tBc54Fcg34PPlUCcYuUaTcAs3acYZc5oUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5cYuUaTcCticgticiYFBTrIcurUC3rTcFYThCcGNbylBrch-hDoGo4ZHhrhhaFhrhrhhacBrWahrhrBi5gUsPWgithrFB5b-5iVpyU_~Ew"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifr1Eci2j-w280-h280/asus-vivobook-14x-20.webp",
        "productName": "Asus Vivobook 14X 2023 K3405VF-LY541WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/4 GB Graphics)",
        "price": "₹65,990",
        "rating": "4.3",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6P4HfDU-npJAi4_hrhArnrysuhyihDRPwZw1pwzbh-hrhhaFhrhrhhacBrWahrhrBi5WBunlag5hrFB5yrnsTvqBYzfK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9ORl0Au4-w280-h280/hp-15-fd0024tu-lapto.webp",
        "productName": "HP 15-fd0024TU Laptop (13th Gen Core i7/ 16GB/ 512 GB SSD/ Win11 Home)",
        "price": "₹74,990",
        "rating": "4.45",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrO4U1uHmH_jWPJihrhAgTYBOr3Uh7tBc54FcoPoZcYuUaTcAs3acYGc5ZUtcWauc5ZbPBc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54cgiPPoHUCcUtYucTYWtUcTrBUshDhDh8GPGriio6ZgHGlhmBYihkwkp7.07Sze-Sd.fShrhhaFhrhrhhacBrWahrhrBi55Puuyl63hrFB5K1kK8Hi7akBI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTEvU8GNT-w280-h280/asus-tuf-gaming-f17.webp",
        "productName": "Asus TUF Gaming F17 FX706HF-HX018W Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹48,990",
        "rating": "4.5",
        "specScore": "60",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq9~HUPJ87pnNKxhrhArnrysuhyihDRPwoG0ddJSh-hrhhaFhrhrhhacBrWahrhrBi5iX5ra6PNhrFB5aP.yPTCE-mHj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUTVSp1Ba-w280-h280/hp-15-eg3036tu-lapto.webp",
        "productName": "HP 15-eg3036TU Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹83,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6Px8syij7I~vY15hrhArnrysuhyihDRPwZ044bJ7h-hrhhaFhrhrhhacBrWahrhrBi58U8aI8AghrFB5RRpAR3AUV7Ay"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGgkJ0ep2-w280-h280/msi-cyborg-15-a12ucx.webp",
        "productName": "MSI Cyborg 15 A12UCX-264IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹54,990",
        "rating": "4.6",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Nvidia GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpE2kaIdqO7rnUhrhArnrysuhyihDRPwZS.XomSh-hrhhaFhrhrhhacBrWahrhrBi54s6rbD8YhrFB5k9xP_gj55DN6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iko1kN8N5-w280-h280/hp-victus-15-fa0998t.webp",
        "productName": "HP Victus 15-fa0998TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹65,990",
        "rating": "4.7",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqeNx4PfjHvrQpyhrhArnrysuhyihDRPKlSpoXz5h-hrhhaFhrhrhhacBrWahrhrBi5W4NFGZg3hrFB5XuXsSmPyzoa_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGTq3pNSl-w280-h280/lenovo-v15-82qya00mi.webp",
        "productName": "Lenovo V15 82QYA00MIN Laptop (Celeron N4020/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹22,730",
        "rating": "4.2",
        "specScore": "41",
        "features": [
            "Intel Celeron  N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqZBOpBC..VAzw1hrhArnrysuhyihDRPwoXxV-_7h-hrhhaFhrhrhhacBrWahrhrBi5sloDZC6thrFB5_Aued7T~vB5b"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyjzQ7ALu-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED 2023 S5504VA-MA543WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹74,990",
        "rating": "4.35",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFAUT~.2_3x8_YehrhAgTYBOr3Uh7rFCFc2Y2s6ssOcFc54csTaicoPoZcYuUaTca2sctcFa3YaFcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacF44PH2rcnr4H58FcUtYucTYWtUcTrBUshDhDh8XHXbi4lHgg4b6hmBYihkwkpSfJeJSz7_XRJ7hrhhaFhrhrhhacBrWahrhrBi5HYWl6rDYhrFB5fkP7Z9w4sQ6P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibZvrxnje-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 OLED 2023 E1504FA-LK541WS Laptop (Ryzen 5 7520U / 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,790",
        "rating": "4.2",
        "specScore": "55",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1qA1Iy_.dGAqrhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54csTaicoPoZcrnic3Iyauc4cNCricAs3acG4oPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcTO4Ho8FcUtYucTYWtUcTrBUshDhDh8PHHrio5lo55ZPhmBYihkwkp7p7_xe7-ee77KhrhhaFhrhrhhacBrWahrhrBi5Ba2bObs5hrFB5-wffoH6w7HB_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1r3H2L4w-w280-h280/msi-modern-14-c7m-06.webp",
        "productName": "MSI Modern 14 C7M-063IN Laptop (Ryzen 5 7530U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹31,990",
        "rating": "4.3",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQWIqU13RC3RO.xhrhAgTYBOr3Uh7nFYcnsia3uc5Hcrnic3Iyauc4ctaDrcAs3acG4ZPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacAGncPbZYucUtYucTYWtUcTrBUshDhDh8rlr6iXbAlAPllhmBYihkwkp7p0b0S71j7144hrhhaFhrhrhhacBrWahrhrBi5NDPGFbWChrFB5tbeN9_uCIgiW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWQArm7mZ-w280-h280/hp-pavilion-plus-14.webp",
        "productName": "HP Pavilion Plus 14-eh0037TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹74,490",
        "rating": "4",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqfb.lBlWTk0gUKhrhArnrysuhyihDRPR1b0GXxHh-hrhhaFhrhrhhacBrWahrhrBi5ZQDOANgthrFB57kK51DaKO~AW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYn3CcnMP-w280-h280/hp-pavilion-14-dv201.webp",
        "productName": "HP Pavilion 14-dv2014TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹61,400",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PZZF2QaxdwAPyrhrhArnrysuhyihDRPR5plSfRzh-hrhhaFhrhrhhacBrWahrhrBi5ZDOi55FThrFB5F6BAEXn0qR-I"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTNWwbPYX-w280-h280/dell-latitude-3430-l.webp",
        "productName": "Dell Latitude 3430 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹1,08,000",
        "rating": "4.35",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DDell%2520Latitude%25203430%2520Laptop%2520(12th%2520Gen%2520Core%2520i5%252F%25208GB%252F%2520512GB%2520SSD%252F%2520Win11%2520Pro)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0OO2AgHE-w280-h280/agb-octev-vr-1818-ga.webp",
        "productName": "AGB Octev VR-1818 Gaming Laptop (11th Gen Core i7/ 32GB/ 1TB SSD/ Win 10 Pro/ 2GB Graph)",
        "price": "₹40,000",
        "rating": "4.35",
        "specScore": "62",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "32 GB DDR4 RAM",
            "1 TB SSD",
            "2 GB NVIDIA Geforce MX450",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwftVH~miDYvlmnhrhArnrysuhyihDRPle.l.vSlh-hrhhaFhrhrhhacBrWahrhrBi5CZBNtsZ3hrFB5Hjg_K5_txylY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqCszh3UH-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED S3502ZA-L701WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹72,990",
        "rating": "4.25",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris XE Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIzNvsai.y2GAQXhrhArnrysuhyihDRPR7~4Xl4Rh-hrhhaFhrhrhhacBrWahrhrBi5rCQPUO4WhrFB5JYHOkm4mz_14"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYj7QEC3m-w280-h280/hp-omen-16-n0079ax-g.webp",
        "productName": "HP Omen 16-n0079AX Gaming Laptop (AMD Ryzen 7 6800H/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹86,488",
        "rating": "4.25",
        "specScore": "73",
        "features": [
            "6th Gen AMD Ryzen 7  6800H",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB AMD Radeon RX 6650M",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqaUCYXz3e.fax6hrhArnrysuhyihDRPK4.pZRlvh-hrhhaFhrhrhhacBrWahrhrBi5s8gZiZYihrFB5FO4SzK.BPevO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itvl6kLr2-w280-h280/agb-octev-ga-9009-ga.webp",
        "productName": "AGB Octev GA-9009 Gaming Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win 10 Pro/ 2GB Graph)",
        "price": "₹35,000",
        "rating": "4.1",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "2 GB NVIDIA Geforce MX450",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw0H.k0QzTd.lSahrhArnrysuhyihDRPlzoV1Z0Kh-hrhhaFhrhrhhacBrWahrhrBi5UaTXngYWhrFB5ZfPsFWT_9JOe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAUGgTVix-w280-h280/hp-victus-15-fb0050a.webp",
        "productName": "HP Victus 15-fb0050AX Gaming Laptop (AMD Ryzen 5 5600H/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹57,990",
        "rating": "4.4",
        "specScore": "63",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqd3wUFeRfF4N-vhrhArnrysuhyihDRPR4vlGHl4h-hrhhaFhrhrhhacBrWahrhrBi5gDWalnYlhrFB5ygr8AGgS2I3j"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRqBQkcGT-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-57G UN.K9TSI.002 Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹59,990",
        "rating": "4",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PPyYeqFmkllquFhrhArnrysuhyihDRPR4Vze0z7h-hrhhaFhrhrhhacBrWahrhrBi5ZOHrt8NGhrFB5oDrxDEm~u91y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8ASnvrpM-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2022 Laptop (Apple M2/ 8GB/ 512GB SSD/ MacOS)",
        "price": "₹1,02,990",
        "rating": "4.2",
        "specScore": "42",
        "features": [
            "Apple M2 Apple M2 Chip",
            "Octa Core",
            "8 GB Unified Memory RAM",
            "512 GB SSD",
            "10-Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFw~uVaQFDI.0ujmfIhrhAgTYBOr3Uh7rBBTacoPoocnrA6ssOcrY3cnocXcW6c45ocW6cFFicnrAcsFcnsuhUaIcnTDDZtucrh-hDh8AG5aHZG5rgHZbhmBYihkwkp7xRo7dJddlKdXhrhhaFhrhrhhacBrWahrhrBi5CiW6G4iyhrFB5U0xG5rTS5xYp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixjDR9NLT-w280-h280/hp-15s-eq2144au-lapt.webp",
        "productName": "HP 15s-eq2144au Laptop (Ryzen 5 5500U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,490",
        "rating": "4.05",
        "specScore": "54",
        "features": [
            "5th Gen AMD Ryzen 5  5500U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbRSXToeBaUtugD6jORRhrhAgTYBOr3Uh7tBcrnic3Iyauc4ctaDrcAs3ac44PPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcaNo5HHrCcUtYucTYWtUcTrBUshDhDh8i4G6H5aiXG4PrhmBYihkwkp7RSl-K107KXRShrhhaFhrhrhhacBrWahrhrBi5sFbUPl3nhrFB5l7p38j0xCmuR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAKMUE8VT-w280-h280/hp-15s-eq2143au-lapt.webp",
        "productName": "HP 15s-eq2143au Laptop (Ryzen 3 5300U/ 8GB/ 512GB SSD/ Windows 11 Home)",
        "price": "₹29,990",
        "rating": "4.55",
        "specScore": "50",
        "features": [
            "5th Gen AMD Ryzen 3  5300U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GPr6216iXGOpWAhrhAA3snrh7tBc54FcaNo5HZrCcrnic3IyaucZc4ZPPCcUtYucTYWtUcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoP5lcurUC3rTcFYThCc5cblcOWch-hDoHXPoPhrhhaFhrhrhhacBrWahrhrBi5OIrXt6iXhrFB5dlnNrpXHUejq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAMLtuf7b-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS1FQ00 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹68,990",
        "rating": "4.75",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwsvz464H7aAOA3hrhArnrysuhyihDRPKwbevzz4h-hrhhaFhrhrhhacBrWahrhrBi5F5no3WgshrFB53~6e96x98Qkp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaqYZYPMN-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS13J00 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹89,990",
        "rating": "4.1",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKPWPAf1dRuHPmuhrhArnrysuhyihDRPKl~1-HJlh-hrhhaFhrhrhhacBrWahrhrBi55y6BiYy6hrFB5Dgx06TrgBYYx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizWzm3cu-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-79G UN.34NSI.002 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,990",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY7AdT25EXdb5rGhrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrG54cGlWcWrnhNcTrBUshDhDh8XoPX5PoAlGgllhmBYihkwkpSZ7lb-Gwqb.1ShrhhaFhrhrhhacBrWahrhrBi5rY2B36l6hrFB5fpqYlTNnQJKR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizWzm3cu-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-79G UN.34NSI.001 Gaming Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹57,990",
        "rating": "4.6",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYxYwbvp8rSFJ.4hrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrG54cGlWcWrnhNcTrBUshDhDh8riHPXGlG4PoaPhmBYihkwkpSZ7lbw.dSjv-.hrhhaFhrhrhhacBrWahrhrBi5nu2U6uaahrFB5eNAVvaIAR8Xr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iizWzm3cu-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-79G UN.34PSI.001 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹64,990",
        "rating": "4.7",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYVxXvBiaVtI5axhrhAgTYBOr3Uh7rAa3crFBY3acGcYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcrG54cGlWcWrnhNcTrBUshDhDh8Hgilgb4oloHPZhmBYihkwkpSZ7lbpf7Je7zxhrhhaFhrhrhhacBrWahrhrBi5i3UB226UhrFB51JlNV5yE0zJK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5gVzq1nL-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS0X900 Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,13,400",
        "rating": "4.3",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzD_3BedJmArmPthrhArnrysuhyihDRPw0~v-~41h-hrhhaFhrhrhhacBrWahrhrBi5AB4BZCgGhrFB56xvRgX_BugAQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOQLPExcQ-w280-h280/dell-xps-13-oxn93451.webp",
        "productName": "Dell XPS 13 OXN9345140001RIN AI Laptops (Snapdragon X Elite X1E-80-100/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,53,899",
        "rating": "4.4",
        "specScore": "68",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-80-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.4 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ808aid22fGYGOmI0Y~hrhAA3snrh7iaTTcDBFc5ZcFurBi3rWsucDcaThscUsCAtFA3aaucUtYucTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5ZcHcYuAtcsTaiciYFBTrIcnFcsggYAacoPo5cW3rBthsc5c5GcOWch-hDZPXbb4hrhhaFhrhrhhacBrWahrhrBi5Xino6ga3hrFB5rG1tDq4Fmrwf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTB7ztoGk-w280-h280/hp-victus-15-fa1321t.webp",
        "productName": "HP Victus 15-fa1321TX Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX3050 Graph)",
        "price": "₹93,990",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFsqG9Z6-q-j9~phrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acYGc5ZUtcWauc5ZboPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgr5Zo5UDcWrnhNcTrBUshDhDh8Gr4b5GiHiGAaohmBYihkwkpSxvHxf17JzGJ4hrhhaFhrhrhhacBrWahrhrBi5NAN8lTFPhrFB5KrtFrHe3oQ_o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iS8GOpOg7-w280-h280/lenovo-yoga-7-14iml9.webp",
        "productName": "Lenovo Yoga 7 14IML9 83DJ00AKIN Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹94,990",
        "rating": "4.1",
        "specScore": "59",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Integrated Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0H9ortYB40CJ13ahrhAA3snrh7Taus2scIsWrcGc5HYnTlcYuUaTcAs3acCTU3rc4cUsCAtFA3aaucocYuc5cTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtc8CDWrcsTaiciYFBTrIcnFcsggYAacoPo5cFUs3ncW3aIc5cHlcOWch-hDZPX4XohrhhaFhrhrhhacBrWahrhrBi5G2ntBAyPhrFB5dmt9CORwiv8p"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUePbJSfr-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 FA506NFR-HN259WS Laptop (AMD Ryzen 7 7435HS/ 16GB / 512GB SSD/ Win11 Home / 4GB Graph)",
        "price": "₹61,990",
        "rating": "4.4",
        "specScore": "68",
        "features": [
            "7th Gen AMD Ryzen 7 7435HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GVJOi2y_KI_dZVhrhAA3snrh7rFCFcUCgcWrnhNcr54crnic3IyaucGcWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcoP4PcnFcsggYAactsnachYcFUCiauUcW3rBthschncocZcOWch-hDZPXZPohrhhaFhrhrhhacBrWahrhrBi5CbICgnyPhrFB5bHCmgXC.8d6X"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2hbSTLKp-w280-h280/dell-inspiron-7440-2.webp",
        "productName": "Dell Inspiron 7440 2 in 1 Laptop (Intel Core 5 120U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹84,176",
        "rating": "4.5",
        "specScore": "62",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Graphic",
            "14 inches, 2240 x 1400 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwIGytHv2vSevBxhrhArnrysuhyihDRPKXZKpzpSh-hrhhaFhrhrhhacBrWahrhrBi58Aso4nlFhrFB5apqSHar2jqux"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8ciYKUqH-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 16IMH9 83DC003GIN Laptop (Intel Core Ultra 5/ 16GB RAM/ 512GB SSD/ Win 11)",
        "price": "₹77,490",
        "rating": "4.1",
        "specScore": "47",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HGvA.gEl4kXbrshrhAA3snrh7Taus2scYiarBricFTYnc4c5bYntlcYuUaTcAs3acCTU3rc4cUtYucTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5bcYuAtc8CDWrcYBFciYFBTrIcnFcsggYAacoPo5cATsCicW3aIc5cXocOWch-hDZPGlobhrhhaFhrhrhhacBrWahrhrBi5araZaACnhrFB5Bkjizud_KfiV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaS4JWoj7-w280-h280/lenovo-ideapad-3-82r.webp",
        "productName": "Lenovo IdeaPad 3 82RJ00F1IN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹34,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xNz_wH~xwW5D-5hrhArnrysuhyihDRPK5H.GRRGh-hrhhaFhrhrhhacBrWahrhrBi58TAgYbFUhrFB5~ntZAT3jTU7s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEsHmtLoO-w280-h280/dell-14-vostro-3440.webp",
        "productName": "Dell 14 Vostro 3440 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹50,990",
        "rating": "4.25",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "Intel  Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwa2E.HYdyTByD5hrhArnrysuhyihDRPKHb~5GZbh-hrhhaFhrhrhhacBrWahrhrBi5sP5ui4HHhrFB5epBZl88r3KJx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ie7PDLvw5-w280-h280/hp-14-gr0001tu-lapto.webp",
        "productName": "HP 14-gr0001TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹57,999",
        "rating": "4.6",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK466lvJuV_roRUFhrhAA3snrh7tBc5HcW3PPP5UCcYuUaTcAs3acY4c5ZUtcWaucUtYucTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5cHcOWch-hDZPGlZ5hrhhaFhrhrhhacBrWahrhrBi5gAIBsruAhrFB5vCWF3vQHFmVJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imdvWZ0yx-w280-h280/hp-omnibook-x-14-fe0.webp",
        "productName": "HP OmniBook X 14-fe0121QU AI Laptop (Snapdragon X Elite X1E-78-100/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,37,999",
        "rating": "4.75",
        "specScore": "56",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-78-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "14 inches, 2240 x 1400 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_4WX0eeesWQUyDlhrhArnrysuhyihDRPKXHHoGSbh-hrhhaFhrhrhhacBrWahrhrBi5T2Ns8yGihrFB5R6S~_R5yWOj3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iV1bVCdfI-w280-h280/dell-vostro-5630-bus.webp",
        "productName": "Dell Vostro 5630 Business Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹84,490",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Integrated",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY0NnwysDFx1zSthrhAgTYBOr3Uh7iaTTc2sFU3sc4bZPcYuUaTcAs3acYGc5ZUtcWauc5ZbPBc5bcW6c45ocW6cFFic8Yuis8Fc55cB3sc5bc6CFYuaFFcTrBUshDhDh8GGiabHlaGZZlrhmBYihkwkpSodXf-ed~p-J1hrhhaFhrhrhhacBrWahrhrBi5NybyI3bahrFB5P6g23Q9TIKPz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixui5Zn0B-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-52 Laptop (Intel 12th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹54,990",
        "rating": "4.5",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQCbI4NNokHN0-KhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh85r6ZHr4brooH5hmBYihkwkpSoz1e7Kef~fpShrhhaFhrhrhhacBrWahrhrBi5Gynrni6nhrFB5.nX0WVVB3fXi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ik4Y1QvKF-w280-h280/hp-14-gr1022tu-lapto.webp",
        "productName": "HP 14-gr1022TU Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹70,490",
        "rating": "4.3",
        "specScore": "57",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwN_XVqUt_-S49EhrhArnrysuhyihDRPKX-XS5Z5h-hrhhaFhrhrhhacBrWahrhrBi5GTa2uaXWhrFB514qb_0NkOEOI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGasycaEI-w280-h280/honor-magicbook-art.webp",
        "productName": "Honor MagicBook Art 14 2024 Laptop (Intel Core Ultra 5 125H/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹97,990",
        "rating": "4.3",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel ARC Graphics",
            "14.6 inches, 3120 x 2080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHonor%2520MagicBook%2520Art%252014%25202024%2520Laptop%2520(Intel%2520Core%2520Ultra%25205%2520125H%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAZEG2d4b-w280-h280/lenovo-ideapad-5-14a.webp",
        "productName": "Lenovo Ideapad 5 ‎14AHP9 2-in-1 83DR003DIN Laptop (AMD Ryzen 5 8645HS/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹72,490",
        "rating": "4.5",
        "specScore": "63",
        "features": [
            "8th Gen AMD Ryzen 5 8645HS",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw3v-yYfx4kEr-JhrhArnrysuhyihDRPKHHf-G7bh-hrhhaFhrhrhhacBrWahrhrBi5NT43384bhrFB5w24gaWW7OGO6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQiKawVuP-w280-h280/infinix-zero-book-ul.webp",
        "productName": "Infinix Zero Book Ultra AI ZL514 Laptop (Intel Core Ultra 7 155H/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹69,990",
        "rating": "4.7",
        "specScore": "59",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated Intel Arc",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYp06AJnPw2PnRBhrhAgTYBOr3Uh7YugYuYDcya3sc6ssOcCTU3rcrYcBAcYuUaTcAs3acGc544tc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacyT45HcUtYucTYWtUcTrBUshDhDh8XgbAo5G46gil4hmBYihkwkpSxf.d.7x_~fjXhrhhaFhrhrhhacBrWahrhrBi5sFNQT4AnhrFB5FvA0zmOFtS6b"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVq6X146v-w280-h280/colorful-evol-p15-ga.webp",
        "productName": "Colorful Evol P15 Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹88,990",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY_BDEPvT.IqJUQhrhAgTYBOr3Uh7AsTs3gCTca2sTcB54cYuUaTcAs3acYGc5ZUtcWauc5ZboPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPcr5PoPHlPPPGocWrnhNcTrBUshDhDh8H44rr4PXlZooAhmBYihkwkpSxRS~.-w_-fjGhrhhaFhrhrhhacBrWahrhrBi5OTZPPioshrFB5PpQrxd2BTq7i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFjQEx1MU-w280-h280/lenovo-loq-15arp9-83.webp",
        "productName": "Lenovo LOQ 15ARP9 83JC0031IN Gaming Laptop (AMD Ryzen 5 7235HS/ 12GB/ 512GB SSD/ Win11/ 6GB RTX 3050 Graph)",
        "price": "₹62,490",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "7th Gen AMD Ryzen 5 7235HS",
            "Quad Core, 8 Threads",
            "12 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY-jXN9gkRHpzZxhrhAgTYBOr3Uh7Taus2scTsNcoPoHcrnic3Iyauc4cNCricAs3acGoZ4tFc5ocW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54r3BlcWrnhNcTrBUshDhDh8rgHgaXalXioalhmBYihkwkpSxf.ZK7RKe77fhrhhaFhrhrhhacBrWahrhrBi5UlOQQPynhrFB5B7FGn9eCTpai"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iw58KlAeK-w280-h280/msi-modern-15-h-ai-c.webp",
        "productName": "MSI Modern 15 H AI C1MG-045IN Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹72,990",
        "rating": "4.7",
        "specScore": "60",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw3AG2T3DtN4pY6hrhArnrysuhyihDRPR0JRZ-Hmh-hrhhaFhrhrhhacBrWahrhrBi5BGgilCuyhrFB5.rZD.IbW.x9B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icr0cFt3E-w280-h280/colorful-evol-p15-23.webp",
        "productName": "Colorful Evol P15 23-HE55D16512A-G-IND Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹63,990",
        "rating": "4.25",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY-uoA4sdfgpSXQhrhAgTYBOr3Uh7AsTs3gCTca2sTcB54cYuUaTcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4PcoZcta44i5b45orcWcYuicWrnhNcTrBUshDhDh8iaPoZ4a44GHPghmBYihkwkpSx1dfS.fRxXwxhrhhaFhrhrhhacBrWahrhrBi5WyWBa8CQhrFB5bNp7.5o.I08P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilzdQUmuW-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 E510KA-EJ011WS Laptop (Intel Celeron N4500/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹26,990",
        "rating": "4.55",
        "specScore": "46",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel HD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq4QvJ-dp.RQBIuhrhArnrysuhyihDRPKX5Kvz_~h-hrhhaFhrhrhhacBrWahrhrBi5iGy3bXQPhrFB5O7JuOZ2pJEjA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixX0VTeCc-w280-h280/asus-vivobook-s-15-o.webp",
        "productName": "Asus Vivobook S 15 OLED 2024 S5506MA-MA951WS Laptop (Intel Core Ultra 9 185H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,52,990",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Arc",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG_zxJgikq74gxiShrhAgTYBOr3Uh7rFCFc2Y2s6ssOcFc54csTaicoPoHcrYcBs8ahBcYuUaTca2sctcFa3YaFcAs3acCTU3rclc5X4tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacF44Pbnrcnrl458FcUtYucTYWtUcTrBUshDhDh8H5bZXbballaHZhmBYihkwkpSff.djqS.x7XKhrhhaFhrhrhhacBrWahrhrBi5oPuN5lZUhrFB5FnkCgzBge-p-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDwOzlMAe-w280-h280/dell-g15-5535-gaming.webp",
        "productName": "Dell G15-5535 Gaming Laptop (AMD Ryzen 5 7640HS/ 16GB/ 1TB SSD/ Win11/ RTX 3050 6GB Graph)",
        "price": "₹79,924",
        "rating": "4.65",
        "specScore": "72",
        "features": [
            "7th Gen AMD Ryzen 5 7640HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwCTgue4vkpea7VhrhArnrysuhyihDRPwJ0Vp-GHh-hrhhaFhrhrhhacBrWahrhrBi58CDbY34OhrFB5DmNxmsRCfHZv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6n3dsxpp-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 14IAH8 83EQ0063IN Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹45,490",
        "rating": "4.2",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYXQIa9ajpbpKpdhrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcAs3acY4c5oUtcWauc5oH4PtcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HYrtXcUtYucTYWtUcTrBUshDhDh8GobrA5ZHiP4ZPhmBYihkwkpSxf.Z7.0SZG7fhrhhaFhrhrhhacBrWahrhrBi5ag5iBsQahrFB5IgXHyEy64iol"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQVAokjBI-w280-h280/msi-thin-15-b13uc-20.webp",
        "productName": "MSI Thin 15 B13UC-2019IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹77,990",
        "rating": "4.05",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HGA~0Yu3W8JjjnhrhAA3snrh7nFYcUtYuc54cYuUaTcAs3acYGc5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoPo5cAsFnsFcW3rIc5cXbcOWch-hDZPbbb5hrhhaFhrhrhhacBrWahrhrBi5Wu5ZZ5i6hrFB5l4-F5.~U.TdU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igjcHmPbp-w280-h280/msi-modern-15-h-ai-c.webp",
        "productName": "MSI Modern 15 H AI C1MG-046IN Laptop (Intel Core Ultra 7 155H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹69,990",
        "rating": "4.35",
        "specScore": "59",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwsUf2VCmZr~3g0hrhArnrysuhyihDRPKZJV17R5h-hrhhaFhrhrhhacBrWahrhrBi56IoWPuAHhrFB57HdwF_pvZjE2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSsPalIS5-w280-h280/msi-thin-15-b12ucx-1.webp",
        "productName": "MSI Thin 15 B12UCX-1693IN Gaming Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 4GB RTX 2050 Graph)",
        "price": "₹64,990",
        "rating": "4.65",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "8 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF_P_.IR5nY5ubOhrhAgTYBOr3Uh7nFYcUtYuc54cYuUaTcAs3acYGc5oUtcWauc5ob4PtcXcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc65oCADc5blZYucWrnhNcTrBUshDhDh8rG4l5gbXGrAilhmBYihkwkp7.JZG._bbKRSxhrhhaFhrhrhhacBrWahrhrBi5tX4rigZyhrFB540F84D_Y8BPd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF4ilz6Mg-w280-h280/asus-rog-zephyrus-g1.webp",
        "productName": "Asus ROG Zephyrus G16 OLED 2024 GU605MZ-CO931WS Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹2,89,990",
        "rating": "4.65",
        "specScore": "83",
        "features": [
            "Intel Core Ultra 9 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBWE4koT-Y-fXwFehrhArnrysuhyihDRPKob41oXdh-hrhhaFhrhrhhacBrWahrhrBi5T62HlX2DhrFB5pUktd57DbbIU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYvgvcAnt-w280-h280/hp-victus-15-fa1310t.webp",
        "productName": "HP Victus 15-FA1310TX Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹54,999",
        "rating": "4.4",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZCzsvWpA4_1YbahrhAA3snrh7tBc2YAUCFc54cgr5Z5PUDcYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55cHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcoP4PcnFcsggYAacBa3gs3nruAac6TCacocZGcOWch-hDZPG5oohrhhaFhrhrhhacBrWahrhrBi5nArFNCryhrFB5T6m4XKYDlqFU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0wMXNfJE-w280-h280/msi-titan-18-hx-a14v.webp",
        "productName": "MSI Titan 18 HX A14VHG-207IN Gaming Laptop (14th Gen Core i9/ 64GB/ 2TB SSD/ Win11 Home/ RTX 4080)",
        "price": "₹4,09,990",
        "rating": "4.7",
        "specScore": "96",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "64 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_sVQDz9z~1oAoP3hrhArnrysuhyihDRPw0G4.d_Hh-hrhhaFhrhrhhacBrWahrhrBi5IBy8BOWshrFB50u9U5blgfutX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivsUe0UUZ-w280-h280/asus-tuf-gaming-f17.webp",
        "productName": "Asus TUF Gaming F17 FX706HF-NY040W  Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹56,990",
        "rating": "4.35",
        "specScore": "61",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "17 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520TUF%2520Gaming%2520F17%2520FX706HF-NY040W%2520%2520Laptop%2520(11th%2520Gen%2520Core%2520i5%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11%252F%25204GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJF7hQfWQ-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 np750xgk-lg2in Laptop (Intel Core 5 Processor 120U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹68,999",
        "rating": "4.55",
        "specScore": "55",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125EdUBvokqCts_CzBkpCv-GWBhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHc54cbcYuAtcAs3ac4c5bW6c45oW6cuBG4PDWOcTWoYuh-hrhhaFhrhrhhacBrWahrhrBi5t8uOgnXOhrFB5oINWaTzBsreV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieyvGq0yy-w280-h280/acer-chromebook-plus.webp",
        "productName": "Acer Chromebook Plus 514 CB514-4H ‎NX.KUTSI.002 Laptop (Intel Core i3-N305/ 8GB/ 256GB SSD/ Chrome OS)",
        "price": "₹24,990",
        "rating": "4",
        "specScore": "33",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB  RAM",
            "256 GB SSD",
            "Intel Integarted Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzfCf8S1wV6mSK8hrhAgTYBOr3Uh7rAa3cAt3sna6ssOcBTCFcoPoHcYuUaTcAs3acYZcuZP4cXcW6co4bcW6cFFicAt3snacsFcA645HcHtcZlUGcTrBUshDhDh844HoAAblPPaA5hmBYihkwkpSxwlVqZlJ7SpjhrhhaFhrhrhhacBrWahrhrBi5HTCWrDZPhrFB5qZ1wzkTrJf6R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1z8rLRAk-w280-h280/acer-nitro-v-anv15-5.webp",
        "productName": "Acer Nitro V ANV15-51 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB RTX 4050)",
        "price": "₹94,990",
        "rating": "4.75",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqOZsu4IvJoQqW6hrhArnrysuhyihDRPKoK7G1wlh-hrhhaFhrhrhhacBrWahrhrBi5DONT3uuBhrFB5ffzTAwgZprum"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLRXQEQIc-w280-h280/asus-rog-zephyrus-g1.webp",
        "productName": "Asus ROG Zephyrus G14 GA403UV-QS085WS Gaming Laptop (AMD Ryzen 9 8945HS/ 16GB/ 1TB SSD/ Win11 Home/ 8GB RTX 4060 Graph)",
        "price": "₹1,79,000",
        "rating": "4.55",
        "specScore": "75",
        "features": [
            "8th Gen AMD Ryzen 9 8945HS",
            "Octa Core, 16 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9XwVAa6O_fZ4wpCihrhArnrysuhyihDRPK4l1f1x_h-hrhhaFhrhrhhacBrWahrhrBi5TWWXnIaWhrFB5TS.Y6T5Xv1io"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9Tl7ZtcU-w280-h280/asus-rog-strix-g16-g.webp",
        "productName": "Asus ROG Strix G16 G614JI-BG711WS Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,61,990",
        "rating": "4.55",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgn4t5Fnf.v3Ce-fhrhAA3snrh7rFCFc3sWcFU3YDcW5bcYuUaTcAs3acYGc5ZUtcWaucWrnhNcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnacXW6cW3rBtYAFc5bcYuAtc5b4ctycgCTTcticBTCFciYFBTrIcu2YiYrcWags3Aac3UDcHPGPcnFcsggYAactsnachYcFUCiauUcaATYBFacW3rIcoc4cOWch-hDZPbbGHhrhhaFhrhrhhacBrWahrhrBi5QIoNG84DhrFB5nRkDGBf0fKnI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGw6LFibk-w280-h280/dell-vostro-3530-vn3.webp",
        "productName": "Dell Vostro 3530 VN3530KCKC9001ORB1 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹54,697",
        "rating": "4.3",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpkJyG4n.vOO11hrhArnrysuhyihDRPKHb~~SJbh-hrhhaFhrhrhhacBrWahrhrBi536sylNOZhrFB5kwT6BE2Iy5~J"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGw6LFibk-w280-h280/dell-vostro-3530-vn3.webp",
        "productName": "Dell Vostro 3530 VN3530602PF001ORB1 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹49,990",
        "rating": "4.55",
        "specScore": "56",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFdE.Zvsm0Bxo~ChrhAgTYBOr3Uh7iaTTcYuUaTcAs3acY4c5ZUtcWauc5ZZHCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac2sFU3scZ4ZPcUtYucTYWtUcTrBUshDhDh8GlAibAll5l5a4hmBYihkwkpSxo-f-_f7G-4zhrhhaFhrhrhhacBrWahrhrBi56sbrlsQghrFB5Tktd96oXXFw_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilmAgdOwo-w280-h280/acer-al15g-52-gaming.webp",
        "productName": "Acer ‎AL15G- 52 Gaming Laptop (12th Gen Core i5-12450H/ 16GB/ 512GB SSD/ Win11/ 6GB RTX 3050 Graphics)",
        "price": "₹61,990",
        "rating": "4.25",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwT7sx~9j3xf36dhrhArnrysuhyihDRPKZozf5bwh-hrhhaFhrhrhhacBrWahrhrBi5y8l3Go4ThrFB5yg7xl-AN~3Gr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivryxnCD9-w280-h280/lenovo-ideapad-flex.webp",
        "productName": "Lenovo IdeaPad Flex 5 14ALC7 82R900FYIN Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹65,690",
        "rating": "4.15",
        "specScore": "65",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HPY_oPwI0dfSwehrhAA3snrh7Taus2scYiarBricgTaDc4c5HrTAGcrnic3IyauGcUsCAtFA3aaucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtc8CDWrcYBFciYFBTrIcnFcsggYAacoPo5cFUs3ncW3aIc5c44cOWch-hDZPbZb4hrhhaFhrhrhhacBrWahrhrBi5Ulguy8nIhrFB5KrdaCkO1sYvi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGXa1xqbZ-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15 B12MO-817IN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,990",
        "rating": "4.65",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqquVK4CnZXYz6yhrhArnrysuhyihDRPK50VZS~Gh-hrhhaFhrhrhhacBrWahrhrBi5iyQWrraohrFB50HNtRmJeD-js"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icP26XxMw-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 (Snapdragon X Plus/ 16GB/ 256GB SSD/ Win11)",
        "price": "₹1,13,990",
        "rating": "4.2",
        "specScore": "45",
        "features": [
            "Qualcomm Snapdragon X Plus",
            "16 GB LPDDR5x RAM",
            "256 GB SSD",
            "Qualcomm Adreno GPU",
            "13.8 inches, 2304 x 1536 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgWb.DtVyzG16b2IhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcBTCFcUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6co4bW6cFFic8Yuis8Fc55ctsnac5ZcXcYuAtcTAiciYFBTrIcBTrUYuCnc5cZHcOWch-hDZPX45PhrhhaFhrhrhhacBrWahrhrBi5Q4645Y3ZhrFB566SEOIYgp1Jy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihVZDo1T9-w280-h280/asus-vivobook-s-15-o.webp",
        "productName": "Asus Vivobook S 15 OLED 2024 S5506MA-MA552WS Laptop (Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹96,990",
        "rating": "4.45",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 5 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Arc",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYAsygX_Ob~2nE1hrhAgTYBOr3Uh7rFCFc2Y2s6ssOcFc54csTaicoPoHcrYcBs8ahBcYuUaTca2sctcFa3YaFcAs3acCTU3rc4c5o4tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacF44Pbnrcnr44o8FcUtYucTYWtUcTrBUshDhDh8iH4lgo44riAAohmBYihkwkpSff.d1z~x~_.fhrhhaFhrhrhhacBrWahrhrBi5sXa64nnNhrFB5GAl5pSNtsISY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMZ7egyjJ-w280-h280/asus-vivobook-s-16-o.webp",
        "productName": "ASUS Vivobook S 16 OLED 2024 S5606MA-MX551WS Laptop (Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,02,990",
        "rating": "4.5",
        "specScore": "60",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBxFW3geXd49620PhrhArnrysuhyihDRPKZm0Rxoxh-hrhhaFhrhrhhacBrWahrhrBi5grTOnGTPhrFB5b8Ue_QgRWNzk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iudDRGiwm-w280-h280/msi-prestige-14-ai-s.webp",
        "productName": "MSI Prestige 14 AI Studio C1UDXG-030IN Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11 Home/ 6 GB Graphics)",
        "price": "₹1,27,990",
        "rating": "4.75",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Hv_bYUX-wFKpz~hrhArnrysuhyihDRPKoSffxJZh-hrhhaFhrhrhhacBrWahrhrBi5Pn4TFWFuhrFB5WP2Aoo5HH9QQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifo77Z7kt-w280-h280/lenovo-legion-7-16ir.webp",
        "productName": "Lenovo Legion 7 16IRX9 83FD0010IN Gaming Laptop (14th Gen Core i7/ 32GB/ 1TB SSD/ Win11/ 8GB RTX 4070 Graph)",
        "price": "₹1,97,490",
        "rating": "4.75",
        "specScore": "88",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv76gviISuYrHO_E8JohrhAgTYBOr3Uh7Taus2scTaWh3cGcoPoHcYuUaTcAs3acYGc5HUtcWauc5HGPPtDcZocW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPGPc5bY3DlcWrnhNcTrBUshDhDh8bX4Ga4AAZPbAAhmBYihkwkp7fex7HHq.Xx--hrhhaFhrhrhhacBrWahrhrBi5NBWaNAnOhrFB5gfuikKF.i-ye"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iw5nDw0Yt-w280-h280/hp-omen-16-wf0148tx.webp",
        "productName": "HP Omen 16-wf0148TX Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,59,990",
        "rating": "4",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9B2f4e8XwAQFsmYRhrhArnrysuhyihDRPKoKK-51dh-hrhhaFhrhrhhacBrWahrhrBi53h86A5BhrFB5NPrmrAIF7bOC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOlyd2tQe-w280-h280/lenovo-ideapad-flex.webp",
        "productName": "Lenovo IdeaPad Flex 5 14ALC7 82R9005JIN Laptop (AMD Ryzen 5 5500U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹58,490",
        "rating": "4.4",
        "specScore": "65",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ2O_EOBkFWUvT-hrhAgTYBOr3Uh7Taus2scYiarBricrnic3Iyauc4ctaDrcAs3ac44PPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HrTAGcUtYucTYWtUcTrBUshDhDh8X6gHP5oGZ5orrhmBYihkwkpSfl.XwR77e.S4hrhhaFhrhrhhacBrWahrhrBi5HAQrOX8NhrFB5JTa.g~iYqp7P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOcnXVdrE-w280-h280/infinix-inbook-x3-sl.webp",
        "productName": "Infinix INBook X3 Slim XL422 Laptop (12th Gen Core i7/ 32GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹49,990",
        "rating": "4.7",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "32 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjQl2-7IZBR7I1hrhAgTYBOr3Uh7YugYuYDcYuUaTcAs3acYGc5o44CcZocW6c45ocW6cFFic8Yuis8Fc55ctsnacDTHoocUtYucTYWtUcTrBUshDhDh8AaPlHPlPgPHbbhmBYihkwkp7z7x7Ge-ExdKShrhhaFhrhrhhacBrWahrhrBi55WZCrrBXhrFB5Yo7b2G-2N6~r"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNPRH6Zwb-w280-h280/msi-thin-15-b12ve-16.webp",
        "productName": "MSI Thin 15 B12VE-1689IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX4050 Graph)",
        "price": "₹69,990",
        "rating": "4.15",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIvGFsKgDmgzGWohrhArnrysuhyihDRPw0lR0vzoh-hrhhaFhrhrhhacBrWahrhrBi5lrUs4U3FhrFB5_~QoEGKs1I9Z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaZJePgQj-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite ‎AL15G- 52 Gaming Laptop (12th Gen Core i5-12450H / 8GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹51,500",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgKvWBxlkIXA2FhrhArnrysuhyihDRPKZoemKG1h-hrhhaFhrhrhhacBrWahrhrBi5TIAYCCAThrFB5WbxfK.NGWko."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQG4zrdwm-w280-h280/msi-katana-17-13vgk.webp",
        "productName": "MSI Katana 17 13VGK-1230IN Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ 8GB RTX 4070 Graph)",
        "price": "₹1,47,990",
        "rating": "4.55",
        "specScore": "79",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "17.3 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_bCWCgQN-NslUf0hrhArnrysuhyihDRPw0~R5bGzh-hrhhaFhrhrhhacBrWahrhrBi53oWbgIAAhrFB57~74b7jIfO~s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ir7LIYdLI-w280-h280/hp-pavilion-plus-16.webp",
        "productName": "HP Pavilion Plus ‎16-ab0016TX Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win 11/ 6GB RTX3050 Graphics)",
        "price": "₹1,03,990",
        "rating": "4.25",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJeT_FC0vev7KBNihrhArnrysuhyihDRPKobGVwHwh-hrhhaFhrhrhhacBrWahrhrBi5u3trYtFlhrFB5Z4.zS9U3OAyk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioA3TG9Q5-w280-h280/msi-thin-15-b13ucx-1.webp",
        "productName": "MSI Thin 15 B13UCX-1807IN Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹54,990",
        "rating": "4.1",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpE2kaIdqO7rnUhrhArnrysuhyihDRPw0lSGzdbh-hrhhaFhrhrhhacBrWahrhrBi5Q4gHGZ8ZhrFB59yxVdFZq6mxk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iI7g7jG1u-w280-h280/asus-tuf-gaming-a15.webp",
        "productName": "Asus TUF Gaming A15 2024  FA507UI-LP066WS Gaming Laptop (AMD Ryzen 9 8945H/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,41,990",
        "rating": "4.55",
        "specScore": "75",
        "features": [
            "9th Gen AMD Ryzen 9 8945H",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgQA_K22Nfu2ISJehrhAA3snrh7rFCFcUCgcrnic3IyaulcWrnhNcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55cXW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcHPGPcnFcsggYAacnaAtrcW3rIcococOWch-hDZPbHG4hrhhaFhrhrhhacBrWahrhrBi5n6BsOBNthrFB5BGJEj~nxgsJO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ix1L7LnHo-w280-h280/asus-rog-strix-g16-2.webp",
        "productName": "Asus ROG Strix G16 2023 G614JIR-N4062WS Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,99,990",
        "rating": "4.75",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NPE1HBBAa5OWt9dhrhArnrysuhyihDRPKo404peph-hrhhaFhrhrhhacBrWahrhrBi5uYnTD8G8hrFB5ax9lBrKRFD13"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTlkLGBIM-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-52 Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹50,990",
        "rating": "4.45",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbRSXToAHmJ_asZyQu2zhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh8Xib5ZrgX4HXHZhmBYihkwkpSoz1ebqfS.pSxhrhhaFhrhrhhacBrWahrhrBi5TDQ2YHaNhrFB5tUZXjDs8vjWU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFy7XXijx-w280-h280/dell-g15-5530-gaming.webp",
        "productName": "Dell G15 5530 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ RTX 4060 8GB Graph)",
        "price": "₹1,21,719",
        "rating": "4.55",
        "specScore": "74",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB9queDyUDQ402gOhrhArnrysuhyihDRPKRmSel5_h-hrhhaFhrhrhhacBrWahrhrBi5UyCrN3ilhrFB5JbiGa27_GQ5s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyv4mxBqX-w280-h280/hp-pavilion-16-af001.webp",
        "productName": "HP Pavilion 16-af0015TU Laptop (Intel Core Ultra 5 125U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹75,990",
        "rating": "4.1",
        "specScore": "52",
        "features": [
            "Intel Core Ultra 5 Processor 125U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67qEJ~xxr7C9YxdhrhArnrysuhyihDRPKobXSR~fh-hrhhaFhrhrhhacBrWahrhrBi5l5DgynH5hrFB5Dwd~p.5ixxIp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilQfpZWlH-w280-h280/msi-thin-15-b12ve-16.webp",
        "productName": "MSI Thin 15 B12VE-1688IN Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹77,990",
        "rating": "4.1",
        "specScore": "71",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq.ia64DKtHYAtOhrhArnrysuhyihDRPw0lm0.0Hh-hrhhaFhrhrhhacBrWahrhrBi5tPPi8UgWhrFB5SIJi-Bbmn6CB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFs6KHBME-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 NH.QPFSI.001 Gaming Laptop (AMD Ryzen 5 7535HS/ 8GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹64,999",
        "rating": "4.05",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiwBA6pRjFOejpYYUhrhAA3snrh7rAa3cru254cH5c3o2icrnic3Iyauc4cWrnhNcTrBUsBcXW6c45oW6c8Yuis8Fc55cbW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFcTaic6huTYUciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoPo5cs6FYiYruchncoc5PcOWch-hDZPbHHlhrhhaFhrhrhhacBrWahrhrBi58GZ8sWIPhrFB5dKD~OsXWOCps"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLZE7v79a-w280-h280/msi-katana-15-b13vgk.webp",
        "productName": "MSI Katana 15 B13VGK-2009IN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB RTX 4070 Graph)",
        "price": "₹1,35,490",
        "rating": "4.5",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB-BBTDlnpimzYj~hrhArnrysuhyihDRPw0~m-xxxh-hrhhaFhrhrhhacBrWahrhrBi5TUiItn3bhrFB52oB9gCBNdjFP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFs6KHBME-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 NH.QPFSI.003 Gaming Laptop (AMD Ryzen 7 7735HS/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹72,990",
        "rating": "4.25",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY1qjADQA3jgSq2hrhAgTYBOr3Uh7rAa3cuYU3scrnic3IyaucGcsAUrcAs3acGGZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcru254cH5cWrnhNcTrBUshDhDh85ArPaAgGlbZ6ihmBYihkwkp7.dG.X0Gj7zjKhrhhaFhrhrhhacBrWahrhrBi5DGOybssXhrFB5TvVfaZR86_AB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icTMe23Lo-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XE007EIN Laptop (AMD Ryzen 7 7730U/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹63,990",
        "rating": "4.3",
        "specScore": "63",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFJfvOqmTPg~o6qhrhAgTYBOr3Uh7Taus2scrnic3IyaucGcsAUrcAs3acGGZPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5Hr63XcUtYucTYWtUcTrBUshDhDh8H5rAlX44XiGb4hmBYihkwkpSxKK._4odSSf.hrhhaFhrhrhhacBrWahrhrBi5lQBlBUZ2hrFB5P1fZ6ZyCuZgo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixUvnc0JQ-w280-h280/lenovo-legion-5-16ir.webp",
        "productName": "Lenovo Legion 5 16IRX9 83DG004RIN Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,27,490",
        "rating": "4.25",
        "specScore": "75",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_H17if9kUFNHId.hrhArnrysuhyihDRPw_4w.ppJh-hrhhaFhrhrhhacBrWahrhrBi5XbiWXQHthrFB5U9XPy_vxGjzs"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6K5S9MUs-w280-h280/hp-15s-fq5331tu-lapt.webp",
        "productName": "HP 15s-fq5331TU Laptop (12th Gen Core i5/ 8GB/ 1TB SSD/ Win11 Home)",
        "price": "₹51,490",
        "rating": "4.3",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "1 TB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqVDBDkjN9jNf37hrhArnrysuhyihDRPK5HblxJ4h-hrhhaFhrhrhhacBrWahrhrBi5P4aUtUHthrFB5fDWskf~APWsH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEH37Zws0-w280-h280/msi-crosshair-16-hx.webp",
        "productName": "MSI Crosshair 16 HX D14VFKG-206IN Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB RTX4060)",
        "price": "₹1,58,989",
        "rating": "4.55",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBpA2Zdf_Bna~dathrhArnrysuhyihDRPw0m4-mSZh-hrhhaFhrhrhhacBrWahrhrBi5HF4CsUlrhrFB5XtqbSgstHaW0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igqcEknUF-w280-h280/huawei-matebook-x-pr.webp",
        "productName": "Huawei MateBook X Pro 2024 Laptop (Intel Core Ultra 9 185H/ 32GB/ 2TB SSD/ Win11 Home)",
        "price": "₹1,88,990",
        "rating": "4.55",
        "specScore": "74",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB  RAM",
            "2 TB SSD",
            "Intel Arc Graphics",
            "14.2 inches, 3120 x 2080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHuawei%2520MateBook%2520X%2520Pro%25202024%2520Laptop%2520(Intel%2520Core%2520Ultra%25209%2520185H%252F%252032GB%252F%25202TB%2520SSD%252F%2520Win11%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibgcLPSg5-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS008BIN Gaming Laptop (12th Gen Core i5/ 12GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,490",
        "rating": "4.15",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "12 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0Z8.p_2iaEdJbk~hrhAA3snrh7Taus2scTsNc54YrDlcYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBc5oW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcoP4PcnFcsggYAacZb4cTCurcW3aIcocZXcOWch-hDZP4bblhrhhaFhrhrhhacBrWahrhrBi5y2ZaZWNYhrFB5fUbHfHjpsOzC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaUwrVTgC-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00BCIN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050)",
        "price": "₹88,490",
        "rating": "4.25",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC30n-iJnemIE4yxhrhAA3snrh7Taus2scTsNc54Y3DlcYuUaTcAs3acYGc5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacZb4cTCurcW3aIcocZXcOWch-hDZP4blXhrhhaFhrhrhhacBrWahrhrBi5PbYlNBu8hrFB5FXzTmHbD2t8S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuQY6l4zl-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 83DC0003IN Laptop (Intel Core Ultra 5 125H/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹79,990",
        "rating": "4.75",
        "specScore": "52",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwCnnT8a3GxlxO4hrhArnrysuhyihDRPwf7-m_wdh-hrhhaFhrhrhhacBrWahrhrBi5NoBDAIiPhrFB5P59T66kqlPpe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iljDHgZnW-w280-h280/hp-15-fd1098tu-lapto.webp",
        "productName": "HP 15-fd1098TU Laptop (Intel Core Ultra 5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹65,999",
        "rating": "4.3",
        "specScore": "54",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GpmxGSNKRDJgTqhrhAA3snrh7tBcgi5PlXUCcYuUaTcAs3acCTU3rc4cUtYuchYcTYWtUcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5c4lcOWch-hDZP4lGZhrhhaFhrhrhhacBrWahrhrBi5WPPDrliohrFB5O4nmGwEs.CjE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iExibKKXj-w280-h280/dell-alienware-m16-r.webp",
        "productName": "Dell Alienware M16 R2 2024 Gaming Laptop (Intel Core Ultra 9 185H/ 16GB/ 1TB SSD/ Win 11/ 8GB RTX4060)",
        "price": "₹1,65,990",
        "rating": "4.65",
        "specScore": "74",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GEFORCE RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJrpuOvQn1av.sGHhrhArnrysuhyihDRPwfm_X__-h-hrhhaFhrhrhhacBrWahrhrBi56Ug64n8ihrFB5UijsOejWXeoO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0EejJDIU-w280-h280/hp-15-fd0220tu-lapto.webp",
        "productName": "HP 15-fd0220TU Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,990",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzBWosiPKPlFooohrhAgTYBOr3Uh7tBcYuUaTcAs3acY4c5ZUtcWauc5ZZHCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54cgiPooPUCcUtYucTYWtUcTrBUshDhDh8GilbblrHZo4A6hmBYihkwkp7fS14.JSej7e-hrhhaFhrhrhhacBrWahrhrBi55IP5D6AGhrFB5jQ8AjpTQVsOp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYiAoqRDi-w280-h280/acer-swift-go-14-ole.webp",
        "productName": "Acer Swift Go 14 OLED SFG14-73 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹94,990",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB  RAM",
            "1 TB SSD",
            "Intel Integrated ARC Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKH9T9z5_kG2aG8hrhArnrysuhyihDRPwfS7RZV-h-hrhhaFhrhrhhacBrWahrhrBi5uX3GDHrihrFB53aSWmAAAH-0b"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSM55pRE2-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 3 Pro 14 ‎NP944XFG-KC1IN Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,09,999",
        "rating": "4.3",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "‎Intel Iris Xe Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzVCYQtoQv9_9v-hrhArnrysuhyihDRPw7SeKbJKh-hrhhaFhrhrhhacBrWahrhrBi5gHGlilAThrFB5kg7a.FgiSsmN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4bPt9lXm-w280-h280/lenovo-yoga-slim-7-8.webp",
        "productName": "Lenovo Yoga Slim 7 83CV002DIN Laptop ( Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,05,799",
        "rating": "4.4",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Integrated Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_rrIWgqgbWNyzIChrhArnrysuhyihDRPwzp~Km~_h-hrhhaFhrhrhhacBrWahrhrBi5tus6PB5ghrFB5v~kW.vaWYn9d"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy8rqRDtT-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 ‎PHN16-72 2024 Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,47,980",
        "rating": "4",
        "specScore": "78",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_gQ2SjtvzJywYXkhrhArnrysuhyihDRPw_1_JH0fh-hrhhaFhrhrhhacBrWahrhrBi5iFsOIOYDhrFB5ydoGODrO0e_3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-id5q7gFSP-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 3 5300U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹28,990",
        "rating": "4.05",
        "specScore": "54",
        "features": [
            "5th Gen AMD Ryzen 3 5300U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afryY3DHguJ1my6PphrhArnrysuhyihDRPwJzex5zVh-hrhhaFhrhrhhacBrWahrhrBi5HD6urn3UhrFB5Jms9P2r8V3tq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ie85wUMvc-w280-h280/hp-envy-x360-14-fc01.webp",
        "productName": "HP Envy x360 14-fc0105TU Laptop (Intel Core Ultra 5 125U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹89,999",
        "rating": "4.6",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 5 125U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3J1V_Yzo6kowO.hrhAA3snrh7tBcau2IcDZbPcYuUaTcAs3acCTU3rc4cUsCAtFA3aaucocYuc5cTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtc8CDWrcYBFciYFBTrIcnFcsggYAacoPo5crUnsFBta3YAc6TCac5cHHcOWch-hDZP4XZbhrhhaFhrhrhhacBrWahrhrBi5t223XDyDhrFB5Px.uptTt1DDo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioGGCa7zG-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGK-KS1IN Laptop (Intel Core 5 Processor 120U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹64,990",
        "rating": "4.65",
        "specScore": "53",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58Jalq3eN8aHuHZGShrhAgTYBOr3Uh7FrnFCuWcWrTrDIc6ssOHcYuUaTcAs3ac4c5oPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacuBG4PDWOcOF5YucuBG4PDWOcTF5YucUtYucTYWtUcTrBUshDhDh8aZZ5AZZHH5o6XhmBYihkwkp7f~ob.VEJE~7ehrhhaFhrhrhhacBrWahrhrBi5CWQ8UolAhrFB5Cx_ibwkFqGf3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iR52l07by-w280-h280/hp-omen-transcend-14.webp",
        "productName": "HP Omen Transcend 14-fb0007TX Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,54,990",
        "rating": "4.65",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_G36lGXF876oHd~hrhArnrysuhyihDRPw_1f5ezVh-hrhhaFhrhrhhacBrWahrhrBi5ZB4WnB63hrFB51E6qFbPdRAAA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifMmN7fK8-w280-h280/hp-pavilion-15-eg303.webp",
        "productName": "HP Pavilion 15-eg3032TU Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹77,990",
        "rating": "4.7",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK4udEPmOTs3-kvehrhAA3snrh7tBc54caWZPZoUCcYuUaTcAs3acYGc5ZUtcWaucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5bW6cW3rBtYAFc54cbcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5cG4cOWch-hDZP44GGhrhhaFhrhrhhacBrWahrhrBi5IY2nruAuhrFB5nfBkwng7YZVu"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idKr4esFi-w280-h280/infinix-inbook-y4-ma.webp",
        "productName": "Infinix INBook Y4 Max Series YL613 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹31,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY5KRknCSn8kJ9.hrhAgTYBOr3Uh7YugYuYDcIHcnrDcFa3YaFcYuUaTcAs3acYZc5ZUtcWauc5Z54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacITb5ZcUtYucTYWtUcTrBUshDhDh8gPgl5GP6ZArlghmBYihkwkp7JJRvE.vEVJSfhrhhaFhrhrhhacBrWahrhrBi5ZuGTsZgahrFB5f3fQ_k-qpltw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0Jlk1ahz-w280-h280/honor-magicbook-x14.webp",
        "productName": "Honor MagicBook X14 Pro 2024 ‎FRI-G56 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDRx4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwtaZ.0WPaCtKBqhrhArnrysuhyihDRPw_mdbKGJh-hrhhaFhrhrhhacBrWahrhrBi5BalYiDPQhrFB5ydt~R_d1P16t"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isUfmjfOH-w280-h280/honor-magicbook-x16.webp",
        "productName": "Honor MagicBook X16 Pro 2024 ‎BRN-G56 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹58,990",
        "rating": "4.4",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwYfxqyVfwyCpfShrhArnrysuhyihDRPw_mJ_fR5h-hrhhaFhrhrhhacBrWahrhrBi5uFWAbXgAhrFB54E36JkOiveQS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izuhiiNsA-w280-h280/apple-macbook-air-15.webp",
        "productName": "Apple MacBook Air 15 2024 MRYR3HN/A Laptop (Apple M3/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹1,23,900",
        "rating": "4.1",
        "specScore": "54",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "10-Core GPU",
            "15.3 inches, 2880 x 1864 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_AF2S8sr2jXSW_jhrhArnrysuhyihDRPw_oop0Szh-hrhhaFhrhrhhacBrWahrhrBi5bsGDiANZhrFB5qbeQV_0Keuxg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAbqxfwaA-w280-h280/msi-vector-17-hx-a14.webp",
        "productName": "MSI Vector 17 HX A14VHG-806IN Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹2,79,990",
        "rating": "4.5",
        "specScore": "92",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "17 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJFozSzZjVt3PE5DhrhArnrysuhyihDRPwz~0lmJ.h-hrhhaFhrhrhhacBrWahrhrBi538sHnHQFhrFB5iilyYpr_S0HI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy8Hoa9eH-w280-h280/xiaomi-redmi-book-pr.webp",
        "productName": "Xiaomi Redmi Book Pro 16 2024 Laptop (Intel Core Ultra 5/ 32GB/ 1TB SSD/ Win 11)",
        "price": "₹69,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel  ARC Graphics",
            "16 inches, 3072 x 1920 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520Book%2520Pro%252016%25202024%2520Laptop%2520(Intel%2520Core%2520Ultra%25205%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win%252011)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imyeOTny6-w280-h280/xiaomi-redmi-book-pr.webp",
        "productName": "Xiaomi Redmi Book Pro 14 2024 Laptop (Intel Core Ultra 5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹59,990",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520Book%2520Pro%252014%25202024%2520Laptop%2520(Intel%2520Core%2520Ultra%25205%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win%252011)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUNeywWs1-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 360 NP960QGK-KG2IN Laptop (Intel Core Ultra 7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,79,990",
        "rating": "4.4",
        "specScore": "70",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJjvj70JWadOV~eFFO-hrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3scZbPc5bcYuAtcCTU3rcGc5bW6c5U6cuBlbPNWOcOWoYuh-hrhhaFhrhrhhacBrWahrhrBi5WGbBNOlFhrFB58H-gJpbPeSKb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipaijNV3D-w280-h280/asus-zenbook-14-oled.webp",
        "productName": "Asus Zenbook 14 OLED 2024 UX3405MA-QD552WS Laptop (Intel Core Ultra 5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹99,990",
        "rating": "4.1",
        "specScore": "56",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKb.qzjlU7VIkgJhrhArnrysuhyihDRPw05bRewRh-hrhhaFhrhrhhacBrWahrhrBi5HP2NTIPHhrFB5rfC4tyf7-9iJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1fCFfykQ-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-72T Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹79,880",
        "rating": "4.5",
        "specScore": "56",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated ARC Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PwQB3q-XwOgNJuhrhArnrysuhyihDRPKlwo10dHh-hrhhaFhrhrhhacBrWahrhrBi5B2IFF2YahrFB58-NE~qotQ.6E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGp20wtu6-w280-h280/asus-vivobook-14x-k3.webp",
        "productName": "Asus Vivobook 14X K3405ZF-LY752WS  Laptop (12th Gen Core i7/ 16 GB RAM/ 1TB SSD/ Win 11/ 4 GB Graphics)",
        "price": "₹76,999",
        "rating": "4.2",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEZ7Iywm2GqWBDphrhAgTYBOr3Uh7tBcYuUaTcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcOZHP4ygcTIG4o8FcUtYucTYWtUcTrBUshDhDh8Gilb6goli5HZihmBYihkwkp7_jvSE07.vSVShrhhaFhrhrhhacBrWahrhrBi5uDXuNTZChrFB5jkeQVYlZYt6_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibU1GKF5j-w280-h280/hp-pavilion-x360-14.webp",
        "productName": "HP Pavilion x360 14-ek0183TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹53,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gx_YeuUft0NGeahrhAA3snrh7tBcBr2YTh3cDZbPcYuUaTcAs3acYZc5oUtcWaucUsCAtFA3aaucocYuc5cTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5curUC3rTcFYThCc5c45cOWch-hDZP4PZlhrhhaFhrhrhhacBrWahrhrBi53nG3PyiYhrFB5jXSNEJb4N9KK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9SmpIa1y-w280-h280/infinix-inbook-y4-ma.webp",
        "productName": "Infinix INBook Y4 Max Series YL613 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹49,990",
        "rating": "4.35",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrznDzswormCKJI8hrhAgTYBOr3Uh7YugYuYDcIHcnrDcFa3YaFcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacITb5ZcUtYucTYWtUcTrBUshDhDh8ZAarXibHPZ4lAhmBYihkwkp7JJRv~V7.KeE_hrhhaFhrhrhhacBrWahrhrBi5WDNnu3AuhrFB57JyDtUjqyKwU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifVDHHaGM-w280-h280/dell-g15-5530-gn5530.webp",
        "productName": "Dell G15-5530 GN5530194YM001ORB1 Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ RTX 3050 6GB Graph)",
        "price": "₹95,990",
        "rating": "4.6",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GaPuJYfj_nYACJhrhAA3snrh7iaTTcW54c44ZPcYuUaTcAs3acYGc5ZUtcWaucTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5cir3OcFtris8cW3rIcocXcOWch-hDZPoG4GhrhhaFhrhrhhacBrWahrhrBi5u48atbGChrFB5l4-.PwgN3u04"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7CU2fHPu-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83EM0026IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹58,390",
        "rating": "4.2",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqkbVsmUuwlB69WhrhArnrysuhyihDRPwd0Sb.oHh-hrhhaFhrhrhhacBrWahrhrBi5C6DaCyTbhrFB5mNA0-G_FJzOd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDg9weDfu-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 3 Chrome 14M868 82XJ002LHA Laptop (MediaTek Kompanio 520/ 4GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹19,990",
        "rating": "4.65",
        "specScore": "28",
        "features": [
            "MediaTek Kompanio 520 Kompanio 520",
            "Octa Core",
            "4 GB LPDDR4X RAM",
            "128 GB Hard Disk",
            "Arm Mali G52 MC2 2EE Graphics",
            "14 inches, 1366 x 768 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQfs_FbI-Ibqx1DhrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcnaiYrUaOcOsnBruYsc4oPcHcW6c5oXcW6cannAcFUs3rWacAt3snacsFc5HnXbXcAt3sna6ssOcTrBUshDhDh8HiAbGlllgaZiahmBYihkwkp7effeSveEq7p7hrhhaFhrhrhhacBrWahrhrBi5IiU2nQb3hrFB5FS5H2q4K1fdq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihtZYpu5k-w280-h280/hp-victus-15-fa1124t.webp",
        "productName": "HP Victus 15-fa1124TX Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹57,499",
        "rating": "4.75",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqdWJbKWZsxZprwhrhArnrysuhyihDRPwvbp-.x.h-hrhhaFhrhrhhacBrWahrhrBi5GnyHgAlGhrFB5DrzHSCGHeAgP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieuSWY17D-w280-h280/hp-15s-fr5011tu-lapt.webp",
        "productName": "HP 15s-fr5011TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,690",
        "rating": "4.45",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1we~T26ZZN1GkhrhAgTYBOr3Uh7tBcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54Fcg34P55UCcUtYucTYWtUcTrBUshDhDh86ooogbii446ZXhmBYihkwkp7JpXx.zpG.17vhrhhaFhrhrhhacBrWahrhrBi5YsWGu5yUhrFB5175XPofEfjU~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipav8pOjT-w280-h280/acer-aspire-lite-15.webp",
        "productName": "Acer Aspire Lite 15 AL15-52 Laptop (12th Gen Core i3/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹32,990",
        "rating": "4.4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFq~Wpg78PyHo7rhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54c4ocUtYucTYWtUcTrBUshDhDh8AAiiGolP4llZPhmBYihkwkp7JVxo~f7b_dw.hrhhaFhrhrhhacBrWahrhrBi5ri6rQOaIhrFB5gNZOJkuJKeOv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC7yONe0k-w280-h280/acer-nitro-v-15-anv1.webp",
        "productName": "Acer Nitro V 15 ANV15-51 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹69,990",
        "rating": "4.15",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 SDRAM RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PbF89NA3etZiG6hrhArnrysuhyihDRPw~15zo0Jh-hrhhaFhrhrhhacBrWahrhrBi5XWZHYnoThrFB5xsq81RmmIv4C"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqj6NYyDq-w280-h280/ultimus-lite-nu14u3i.webp",
        "productName": "Ultimus Lite NU14U3INC54BN Laptop (Celeron N4020/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹16,890",
        "rating": "4.45",
        "specScore": "42",
        "features": [
            "Intel Celeron N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated UHD Graphics",
            "14.1 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UKysZWEfUDvml~nhrhArnrysuhyihDRPwHd00Z5eh-hrhhaFhrhrhhacBrWahrhrBi5QIB6lb8GhrFB524ETR3RDTP6o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivl17P4n6-w280-h280/dell-g15-5530-gaming.webp",
        "productName": "Dell G15-5530 Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹83,799",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqia97Ysp0_kI_DhrhArnrysuhyihDRPwKRpG-Zxh-hrhhaFhrhrhhacBrWahrhrBi55QHBWrQNhrFB5kgU7ele5YYId"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8W8XsfUp-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83ER008DIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹51,990",
        "rating": "4.4",
        "specScore": "55",
        "features": [
            "12th Gen intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel IrisXe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmXiUvEfUQqAvqhrhArnrysuhyihDRPwd0S55H0h-hrhhaFhrhrhhacBrWahrhrBi5bBDtZnQThrFB5NS3CHVz.3o5."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ih99gAylz-w280-h280/hp-250-g9-732b6pa-la.webp",
        "productName": "HP 250 G9 732B6PA Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹49,790",
        "rating": "4.45",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjaB8Ul45wANO5hrhAgTYBOr3Uh7tBco4PcWlcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacTrBUshDhDh8larZagiPPPgHAhmBYihkwkp7~e-SE-V~7_l-hrhhaFhrhrhhacBrWahrhrBi5o8IX6lWIhrFB5v2VqwgQOxvHH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFU95CpYT-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 82SB00Y8IN Laptop (AMD Ryzen 7 6800H/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹69,890",
        "rating": "4.45",
        "specScore": "66",
        "features": [
            "6th Gen AMD Ryzen 7 6800H",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzItTJwzgIWTB4jhrhAgTYBOr3Uh7Taus2scYiarBricWrnhNcZcoPoHcrnic3IyaucGcsAUrcAs3acbXPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcY4r3tGiHcTrBUshDhDh8aH4lG4bAgX6gHhmBYihkwkp70~ofqqG.xReJhrhhaFhrhrhhacBrWahrhrBi5lgPYCs3lhrFB5zCPkkkvXvJ4I"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijg5vAqpe-w280-h280/xiaomi-redmi-book-14.webp",
        "productName": "Xiaomi Redmi Book 14 2024 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹49,990",
        "rating": "4",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel ARC Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520Book%252014%25202024%2520Laptop%2520(13th%2520Gen%2520Core%2520i5%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win%252011)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iitsd2But-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XF0077IN Laptop (13th Gen Core i5/ 16 GB RAM/ 1 TB SSD/ Win 11)",
        "price": "₹71,990",
        "rating": "4.45",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF6_z2pvQ_XG9RChrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4coc4OcYBFcYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5bY3TXcUtYucTYWtUcTrBUshDhDh86aliZoolPg4G6hmBYihkwkp70~ofGbSSV7fKhrhhaFhrhrhhacBrWahrhrBi5y3b55Ya4hrFB52jomUoNKqy0H"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEmrHz5Rr-w280-h280/asus-chromebook-cx14.webp",
        "productName": "Asus Chromebook CX1400FKA-EC0168 Laptop (Celeron N4500/ 8GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹26,990",
        "rating": "4.65",
        "specScore": "38",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz.sO6TZQFWfnqIhrhAgTYBOr3Uh7rFCFcAt3sna6ssOcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6c5oXcW6cannAcFUs3rWacAt3snacsFcAD5HPPgOrcaAP5bXcTrBUshDhDh85ZlZo6G5Gi56ZhmBYihkwkp7eSpZ17pfX17lhrhhaFhrhrhhacBrWahrhrBi5i6W2gn5DhrFB5ZzZ.gzH0BKd_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihQzYaPz6-w280-h280/avita-pura-s102-lapt.webp",
        "productName": "Avita Pura S102 Laptop (Celeron N4020/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹17,149",
        "rating": "4.75",
        "specScore": "38",
        "features": [
            "Intel Celeron  N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FD8z.6VSpHktE1PhrhArnrysuhyihDRPwm1l4~7.h-hrhhaFhrhrhhacBrWahrhrBi5i6bAXb8ihrFB5jGxl84RRpzrt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXwF9aXwY-w280-h280/apple-macbook-pro-14.webp",
        "productName": "Apple MacBook Pro 14 2023 Laptop (Apple M3/ 8GB/ 512GB SSD/ macOS)",
        "price": "₹1,55,990",
        "rating": "4.5",
        "specScore": "50",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "8 GB  RAM",
            "512 GB SSD",
            "10 Core GPU",
            "14.2 inches, 3024 x 1964 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_WnOUvafkzwnnsdhrhArnrysuhyihDRPwp4vzmp5h-hrhhaFhrhrhhacBrWahrhrBi5AO4IITWHhrFB5rmrE47636JUO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuWVVgZly-w280-h280/gigabyte-g5-mf-e2in3.webp",
        "productName": "Gigabyte G5 MF-E2IN313SH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹63,990",
        "rating": "4.15",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQyfbbYTSWrl011hrhAgTYBOr3Uh7WYWr6IUacWcFa3YaFcYuUaTcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4PcW4cngcaoYuZ5ZFtcWrnhNcTrBUshDhDh866olZabZgHGGghmBYihkwkp7v4~q7Jb1~1qzhrhhaFhrhrhhacBrWahrhrBi5P5FrTPPUhrFB5NZiaC0D3mPR."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKZvIX3fa-w280-h280/hp-pavilion-plus-16.webp",
        "productName": "HP Pavilion Plus ‎16-ab0456TX Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win 11/ 6GB Graphics)",
        "price": "₹1,14,999",
        "rating": "4",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~x2nZBoDPtqRsUkhrhAgTYBOr3Uh7tBcBr2YTh3cBTCFcYuUaTcAs3acYGc5ZUtcWauc5ZGPPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5bcr6PH4bUDcWrnhNcTrBUshDhDh8a5ZgZXZi6Z4lGhmBYihkwkp70~ofvRv~H.KRhrhhaFhrhrhhacBrWahrhrBi53BtogN4yhrFB522A12lCeODqI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4D4jFYMY-w280-h280/hp-omen-16-xd0007ax.webp",
        "productName": "HP Omen 16-XD0007ax Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,03,490",
        "rating": "4.35",
        "specScore": "72",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_5f_8q4SoWlHAklhrhArnrysuhyihDRPwpZRzH1zh-hrhhaFhrhrhhacBrWahrhrBi5D5n2IUgChrFB5sweD3_SexUAk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuheiy1e3-w280-h280/lenovo-v15-g4-laptop.webp",
        "productName": "Lenovo V15 G4 Laptop (AMD Ryzen 5 7520U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹33,700",
        "rating": "4.65",
        "specScore": "50",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwE10i0J_3zSTnyhrhArnrysuhyihDRPwVzVfRX5h-hrhhaFhrhrhhacBrWahrhrBi5sYAQui4ChrFB5no4_sqZiN1ke"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icDhrRu8A-w280-h280/lenovo-ideapad-1-15a.webp",
        "productName": "Lenovo IdeaPad 1 15AMN7 82VG00ERIN Laptop (AMD Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹31,890",
        "rating": "4.25",
        "specScore": "51",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon 610M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gos2bUWoE50CGPhrhAA3snrh7Taus2scYiarBric5c54rnuGcrnic3IyaucZc54cbcYuAtcXW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5crnic3riasucgticiYFBTrIcATsCicW3aIcXo2WPPa3Yuch-hDZP5HoXhrhhaFhrhrhhacBrWahrhrBi5FADBuiiThrFB5JON.NqYTVP1T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0UU0KgoJ-w280-h280/acer-chromebook-cb31.webp",
        "productName": "Acer Chromebook CB314-3H NX.K04SI.008 Laptop (Intel Celeron N4500/ 8GB/ 64GB SSD/ Chrome OS)",
        "price": "₹15,990",
        "rating": "4.75",
        "specScore": "34",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "64 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1080 x 1920 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UKykGBDu.Y6KtlfhrhArnrysuhyihDRPw--0x7pbh-hrhhaFhrhrhhacBrWahrhrBi5gNlF6Wi2hrFB5BNVJG5_ikJN-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4I3Jn4iY-w280-h280/zebronics-zeb-nbc-2s.webp",
        "productName": "Zebronics ZEB-NBC 2S 2023 Laptop (11th Gen Core i5 / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹26,490",
        "rating": "4",
        "specScore": "55",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq4fir7Zi8Ol13thrhArnrysuhyihDRPwpZVoHl1h-hrhhaFhrhrhhacBrWahrhrBi5325NIr4ahrFB5n-46wZ54mff4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6kXCQGLy-w280-h280/acer-one-11-z8-284-u.webp",
        "productName": "Acer One 11 Z8-284 UN.013SI.032 Laptop ( Intel Celeron N4500/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹18,990",
        "rating": "4.45",
        "specScore": "42",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "11.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FDDKgQvbbwP4xrNhrhArnrysuhyihDRPwSvd~Rwvh-hrhhaFhrhrhhacBrWahrhrBi56lZXoslQhrFB5977jIYSm.sBO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iS8yLUymQ-w280-h280/hp-15s-fq5185tu-lapt.webp",
        "productName": "HP 15s-fq5185TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹34,990",
        "rating": "4.65",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afryn8urVqDpN7yoFhrhArnrysuhyihDRPw-p4-4meh-hrhhaFhrhrhhacBrWahrhrBi5AyZBWTG2hrFB5-UB0sT2E4Y4t"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLi7Ac4g2-w280-h280/zebronics-zeb-nbc-5s.webp",
        "productName": "Zebronics ZEB-NBC 5S 2023 Laptop (12th Gen Core i7 / 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹41,990",
        "rating": "4.45",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqxx~oBOoBRVqG0hrhArnrysuhyihDRPw-lKb0o5h-hrhhaFhrhrhhacBrWahrhrBi5G2oXO2XyhrFB5zvCXA1-81Gt4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifayaBNtQ-w280-h280/hp-15s-fy5007tu-lapt.webp",
        "productName": "HP 15s-fy5007TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹46,990",
        "rating": "4.55",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFpXSfqV_Rt1nCphrhAgTYBOr3Uh7tBcYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgI4PPGUCcUtYucTYWtUcTrBUshDhDh8rXZ5GoPagZPAohmBYihkwkp7z-7lwfzx.S.ohrhhaFhrhrhhacBrWahrhrBi5GOy8uYoChrFB5Ky93Eq_3FtZy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZPbqPaVt-w280-h280/lenovo-ideapad-1-15a.webp",
        "productName": "Lenovo IdeaPad 1 15ALC7 82R400BSIN Laptop (AMD Ryzen 5 5500U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹35,490",
        "rating": "4.3",
        "specScore": "52",
        "features": [
            "5th Gen AMD Ryzen 5  5500U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZYI_0OB_xGx6X8hrhAA3snrh7Taus2scYiarBric5c54rTAGcrnic3Iyauc4c54cbcYuAtcXW6c45oW6c8Yuis8FcnFcsggYAacoPo5crnic3riasucgCTTcticiYFBTrIcW3rBthscW3aIcXo3HPP6FYuch-hDZP5H4bhrhhaFhrhrhhacBrWahrhrBi52YuHIirnhrFB5lBzT2816B_2s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihacaqXRC-w280-h280/dell-inspiron-5430-i.webp",
        "productName": "Dell Inspiron 5430 IN5430FR0KC001ORS1 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹55,999",
        "rating": "4.2",
        "specScore": "50",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpDXpumqF6~iIxhrhArnrysuhyihDRPwoS0eS_bh-hrhhaFhrhrhhacBrWahrhrBi55yXXQPbIhrFB5n~s5wC5-DlGQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilRSmUCwI-w280-h280/lenovo-yoga-7-82yl00.webp",
        "productName": "Lenovo Yoga 7 82YL0099IN Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹99,990",
        "rating": "4.5",
        "specScore": "73",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqnVSDubukxTA8whrhArnrysuhyihDRPw7p4m1Xmh-hrhhaFhrhrhhacBrWahrhrBi5gtyXrOQ4hrFB5mil8AFPe4GTt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDLMz8S9b-w280-h280/acer-travelmate-p2-t.webp",
        "productName": "Acer TravelMate P2 TMP214-53 Business Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹44,990",
        "rating": "4.75",
        "specScore": "62",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq76tfZK3l-lzaZhrhArnrysuhyihDRPwSv1-we7h-hrhhaFhrhrhhacBrWahrhrBi55FFPX3aWhrFB5vXi6KxeTmS-k"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixYukPzD3-w280-h280/primebook-s-wi-fi-la.webp",
        "productName": "Primebook S Wi-Fi Laptop (MediaTek MT8183/ 4GB/ 128GB eMMC/ Prime OS)",
        "price": "₹13,490",
        "rating": "4.15",
        "specScore": "30",
        "features": [
            "MediaTek MT8183",
            "Octa Core",
            "4 GB LPDDR4 RAM",
            "128 GB Hard Disk",
            "ARM Mali G72",
            "11.6 inches, 1366 x 768 pixels",
            "1 Year Warranty",
            "2 USB 3.0 Ports"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UKI-Xq~B-fH1ZvehrhArnrysuhyihDRPKofHVm7dh-hrhhaFhrhrhhacBrWahrhrBi5COlaCgF6hrFB5PWXyzDvWkvkI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifCoQye3o-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82RK00VWIN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,650",
        "rating": "4.7",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "‎Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqj6V0O79SG-vZEhrhArnrysuhyihDRPwvGJ7Xbdh-hrhhaFhrhrhhacBrWahrhrBi5GPPgQT5GhrFB5jBNwXQFse3Oa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF16JlZw8-w280-h280/dell-vostro-3530-lap.webp",
        "productName": "Dell Vostro 3530 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹51,990",
        "rating": "4.4",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmXiUvEfUQqAvqhrhArnrysuhyihDRPwwep0xJeh-hrhhaFhrhrhhacBrWahrhrBi5WyroaigPhrFB53ZJEWyZj8-s9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itaefTpS5-w280-h280/dell-inspiron-15-352.webp",
        "productName": "Dell Inspiron 15 3520 IN352092K4N001ORS1 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹51,890",
        "rating": "4.55",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1YFq2FO3QP.39hrhAgTYBOr3Uh7iaTTcYuFBY3suc54cZ4oPcYuUaTcAs3acY4c5oUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacTrBUshDhDh8PAlZooliP4ogahmBYihkwkp7zq7JbSx47-7~hrhhaFhrhrhhacBrWahrhrBi5rsQUWBlbhrFB5rz7nPuT.9OvQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTQbEh7ax-w280-h280/dell-inspiron-3520-1.webp",
        "productName": "Dell Inspiron 3520 15 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹49,140",
        "rating": "4.15",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwAsyumFqWqHV7shrhArnrysuhyihDRPw-VoXZw5h-hrhhaFhrhrhhacBrWahrhrBi5uluHUBGDhrFB5EQeX0TSpFOJy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5FplYEsQ-w280-h280/asus-rog-strix-g16-2.webp",
        "productName": "Asus ROG Strix G16 2023 G614JJ-N3088WS Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹98,490",
        "rating": "4.6",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqTtkRyDsPanRXthrhArnrysuhyihDRPwvvG_S.dh-hrhhaFhrhrhhacBrWahrhrBi5NX6PWtaNhrFB57YAl_n17lUEO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIAjpeE8x-w280-h280/asus-rog-strix-g16-2.webp",
        "productName": "Asus ROG Strix G16 2023 G614JJ-N3086WS Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹93,990",
        "rating": "4.55",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEKtoouBfHkXnIkhrhAgTYBOr3Uh7rFCFcYuUaTcAs3acY4c5ZUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcWb5HQQcuZPXb8FcWrnhNcTrBUshDhDh8oAGHHraZbAbaXhmBYihkwkp70Vd4KKzSSHRShrhhaFhrhrhhacBrWahrhrBi54WXraWrOhrFB5V_mbndmRSFpt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ig9K401Jc-w280-h280/ultimus-neo-nu14u3in.webp",
        "productName": "Ultimus Neo NU14U3INT54BN Laptop (10th Gen Core i3/ 8GB/ 256GB SSD/Win11 Home)",
        "price": "₹19,990",
        "rating": "4.75",
        "specScore": "47",
        "features": [
            "10th Gen Intel Core i3 1005G1",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated Iris",
            "14.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FDDgT.j2pIotPbphrhArnrysuhyihDRPw7vddf5_h-hrhhaFhrhrhhacBrWahrhrBi5WDA54rQBhrFB5Ynu7af_nN3.o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHdwZgNTp-w280-h280/dell-inspiron-7430-2.webp",
        "productName": "Dell Inspiron 7430 2023 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹97,890",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrO9yyP9xIE4Zfl1hrhAgTYBOr3Uh7iaTTcYuFBY3sucGHZPcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacYAGHZPQ3H2IPP5s3F5coc5cTrBUshDhDh8Ao6r6PirPoaHGhmBYihkwkp7fK.xvdS~o7EfhrhhaFhrhrhhacBrWahrhrBi5AYoOCT22hrFB5~FFIRQp1E~5E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iavkFhb4h-w280-h280/hp-pavilion-x360-14.webp",
        "productName": "HP Pavilion x360 14-ek1021TU Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹84,800",
        "rating": "4.25",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFYQVJB.kGUkjvHhrhAgTYBOr3Uh7tBcBr2YTh3cDZbPcYuUaTcAs3acYGc5ZUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HcaO5Po5UCcoc5cTrBUshDhDh84oGZHPP4HlH6ghmBYihkwkp7zHJ_j_pve..7hrhhaFhrhrhhacBrWahrhrBi5aI4gWQrThrFB50185.kA94-nK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibORU5vQa-w280-h280/hp-pavilion-15-eg301.webp",
        "productName": "HP Pavilion 15-eg3018TU Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹77,490",
        "rating": "4.3",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4- RAM",
            "1 TB SSD",
            "Intel Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYv-B36f7GB-Iw_hrhAgTYBOr3Uh7tBcBr2YTh3coPoHcYuUaTcAs3acY4c5ZUtcWauc5ZZ4Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac54caWZP5XUCcUtYucTYWtUcTrBUshDhDh8roAiZlaar4GlbhmBYihkwkp7eSqlw_4~S11ShrhhaFhrhrhhacBrWahrhrBi5y3tXUAXBhrFB5saNQ4nlKPW9f"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWoMUjbwu-w280-h280/asus-vivobook-pro-15.webp",
        "productName": "Asus Vivobook Pro 15 M6500QC-HN551WS Laptop (AMD Ryzen 5 5600HS/ 16 GB RAM/ 1 TB SSD/ Win 11/ 4 GB Graphics)",
        "price": "₹65,990",
        "rating": "4.7",
        "specScore": "59",
        "features": [
            "5th Gen AMD Ryzen 5 5600HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF_ei1YP9fOi_A7hrhAgTYBOr3Uh7rFCFc2Y2s6ssOcB3sc54cA3arUs3crnic3Iyauc4ctaDrcAs3ac4bPPtFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pcnb4PPNActu4458FcWrnhNcTrBUshDhDh84rgaoGrllPr64hmBYihkwkp7v4~qXJESH-GGhrhhaFhrhrhhacBrWahrhrBi5rbsANWBGhrFB5xDjwGErrq--u"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iT22FRG8W-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XE004QIN Laptop (AMD Ryzen 5 7530U/ 16 GB RAM/ 512 GB SSD/ Win 11)",
        "price": "₹56,389",
        "rating": "4.45",
        "specScore": "57",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYxZ4jst9O5Xz82hrhAgTYBOr3Uh7Taus2scIsWrcbcrnic3Iyauc4ctaDrcAs3acG4ZPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacYiarBricUtYucTYWtUcTrBUshDhDh8aZg4libGZPZ5ahmBYihkwkp7v0p7H~xjjS-_hrhhaFhrhrhhacBrWahrhrBi535DQBGH8hrFB5Oqr2aDTanqS8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i07bZFfM4-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82RK00VVIN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,490",
        "rating": "4.75",
        "specScore": "48",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "‎Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZYI_0OB_xGx6X8hrhAA3snrh7Taus2scYiarBricZcYuUaTcAs3acYZc5oUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5cYuUaTcCticgCTTcticiYFBTrIcr3AUYAcW3aIcXo3OPP22Yuch-hDZPPoZbhrhhaFhrhrhhacBrWahrhrBi5IsyQ56GQhrFB5p6m4AOr74aP9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivBee9CJG-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "Acer Aspire 7 A715-76G NH.QMYSI.001 Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹47,990",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQBr5Oe.ViaTPqZhrhAgTYBOr3Uh7rAa3crFBY3acGcoPoHcYuUaTcAs3acY4c5oUtcWauc5oH4PtcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4PcrG54cGbWc4l8WcWrnhNcTrBUshDhDh8X6H54XGoP6Ha6hmBYihkwkp7vS-EjSpvJzSShrhhaFhrhrhhacBrWahrhrBi5BHrZNsPDhrFB5bsCC_q9uJPan"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRQpo7dU7-w280-h280/hp-victus-15-fb1001a.webp",
        "productName": "HP Victus 15-FB1001AX Gaming Laptop (AMD Ryzen 5 7535HS/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹54,700",
        "rating": "4.45",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQC5lpSg~Z3bj92hrhAgTYBOr3Uh7tBcrnic3Iyauc4ctaDrcAs3acXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFc54cg65PP5rDcTrBUshDhDh8ggXZl5ab6G6XbhmBYihkwkp7e-J1.KZfd-JjhrhhaFhrhrhhacBrWahrhrBi5olrIU6rthrFB5zD~aO.113P9p"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLm4X5yyC-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 90NR0GW1-M00F00 Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹82,990",
        "rating": "4.7",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "20 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "4 GB ‎NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11  OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HRxRRi~5USkjqChrhAA3snrh7rFCFcUCgcWrnhNcg54cYuUaTcAs3acYGc5oUtcWaucWrnhNcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnacHW6cWii3bc54cbcYuAtcgCTTcticYBFciYFBTrIcnFcsggYAacoPo5cnaAtrcW3rIcococOWch-hDoG4GbbhrhhaFhrhrhhacBrWahrhrBi5isNNPOaIhrFB5GiBxflqWJ2qT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIvS15Nj5-w280-h280/asus-chromebook-cx15.webp",
        "productName": "Asus Chromebook CX1500CKA-EJ0277 Laptop (Celeron N4500/ 4GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹18,990",
        "rating": "4.3",
        "specScore": "32",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "4 GB LPDDR4X RAM",
            "128 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtF6k_OwlHXB7iThrhAgTYBOr3Uh7rFCFcAt3sna6ssOcYuUaTcAaTa3suciCrTcAs3acuH4PPcHcW6c5oXcW6cannAcFUs3rWacAt3snacsFcAD54PPAOrcuQPH5ZcTrBUshDhDh8lH4ZiX6Z4Ai6AhmBYihkwkp7eSpZ_.7~4p7zhrhhaFhrhrhhacBrWahrhrBi5bWG25taYhrFB5X-AkWW6FTIo~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ib6jwXU9j-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82XQ0096IN Laptop (AMD Ryzen 5 7520U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹44,490",
        "rating": "4.5",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon 610M Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0Zs1gJAOn_Af6xXhrhAA3snrh7Taus2scYiarBricFTYncZc54rnuXcrnic3Iyauc4c54cbcYuAtc5bW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5crnic3riasucb5PncgticYBFciYFBTrIcr3AUYAcW3aIcXoDNPPlbYuch-hDoG4bX5hrhhaFhrhrhhacBrWahrhrBi5CQ8FWiFWhrFB5JSY1pbojZtGB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSUnkvdbC-w280-h280/hp-victus15-fb0147ax.webp",
        "productName": "HP Victus15-fb0147AX Gaming Laptop (Ryzen 5 5600H/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹47,900",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB AMD Radeon AMD Radeon RX 6500M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFpfFABGHWXBAiIhrhAgTYBOr3Uh7tBcrnic3Iyauc4ctaDrcAs3acXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFc54cg6P5HGrDcTrBUshDhDh8HPa5Pa44AXAGbhmBYihkwkp7e-0wJ7lb17l7hrhhaFhrhrhhacBrWahrhrBi5AbZyiZtUhrFB5o_KfD0Yz0u-m"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iw5mIPUYo-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 14IAH8 83BF0045IN Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹62,490",
        "rating": "4.55",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZyS2fp6SXij6vJhrhAA3snrh7Taus2scYiarBricFTYnc4c5HYrtXcYuUaTcAs3acY4c5oUtcWauc5HcYuAtc5bW6c5U6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcCtic8CDWrcYBFciYFBTrIcATsCicW3aIcXZ6gPPH4Yuch-hDoG4bGlhrhhaFhrhrhhacBrWahrhrBi5uPYWA44NhrFB54tpyF1~ffTrH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7H7Tt4lj-w280-h280/asus-vivobook-go-14.webp",
        "productName": "Asus Vivobook Go 14 2023 E1404FA-NK325WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹32,990",
        "rating": "4.55",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiwBV5dBzvZsANgwUhrhAA3snrh7rFCFc2Y2s6ssOcWscrnic3IyaucZcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticTaic6huTYUciYFBTrIcnFcsggYAacoPo5cnYDaichnc5cZXcOWch-hDZPGll4hrhhaFhrhrhhacBrWahrhrBi5aDbaulg5hrFB5rfT-g9B6ZekR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLhn1DjD8-w280-h280/infinix-inbook-x3-sl.webp",
        "productName": "Infinix INBook X3 Slim XL422 2023 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹29,990",
        "rating": "4.4",
        "specScore": "44",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFRYGpq--pQ1_KEhrhAgTYBOr3Uh7YugYuYDcDZcFTYncYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacDTHoocUtYucTYWtUcTrBUshDhDh8AilGaGrblbGgohmBYihkwkp7veJ_4f1f-Jl7hrhhaFhrhrhhacBrWahrhrBi5XOhuH6PhrFB5e7-n-FRT9VJT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idCk82Xxh-w280-h280/infinix-inbook-x3-sl.webp",
        "productName": "Infinix INBook X3 Slim XL422 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹39,990",
        "rating": "4.4",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrztHxDr9HSp9ndqhrhAgTYBOr3Uh7YugYuYDcDZcFTYncoPoHcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacDTHoocUtYucTYWtUcTrBUshDhDh85gbrbPglAglbrhmBYihkwkp7veJ_RqdKz7KzhrhhaFhrhrhhacBrWahrhrBi535Q6PXtAhrFB5CgBB-PqktH1m"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWuhI8Mja-w280-h280/lenovo-v15-82kb00rji.webp",
        "productName": "Lenovo V15 82KB00RJIH Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹44,990",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwrNaZ~7D5kpxddhrhArnrysuhyihDRPlSHxJlGvh-hrhhaFhrhrhhacBrWahrhrBi5XNuQ2TB2hrFB5BtY_mjtsu1Rj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSa1pvRbX-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 82XE004RIN Laptop (AMD Ryzen 5 7530U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹53,190",
        "rating": "4.75",
        "specScore": "61",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Integrated SoC",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqmT_gqifSVqnsthrhArnrysuhyihDRPwwdvolpbh-hrhhaFhrhrhhacBrWahrhrBi5HWBHiU66hrFB5V_.2oXlYZ2~d"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijzy6NB3Y-w280-h280/hp-victus-15-fa0188t.webp",
        "productName": "HP Victus 15-fa0188TX Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹79,990",
        "rating": "4.2",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEHilp59X._DnsHhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgrP5XXUDcWrnhNcTrBUshDhDh85Aoal56r4ArGahmBYihkwkp7v.~oHR00VRSehrhhaFhrhrhhacBrWahrhrBi5YQrXttbOhrFB5Q74DbgyJGe~m"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDbbwHhWk-w280-h280/lenovo-loq-15irh8-82.webp",
        "productName": "Lenovo LOQ 15IRH8 82XV00F4IN 2023 Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹62,800",
        "rating": "4.35",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFJotjX1s~YmjwAhrhAgTYBOr3Uh7Taus2scTsNcoPoHcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54Y3tXi5cWrnhNcTrBUshDhDh8H6al4gHAH6r4ihmBYihkwkp7vx0R-V0e.VeehrhhaFhrhrhhacBrWahrhrBi5XOT4nZ45hrFB5Y095DTUTAb9G"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikDUMInjl-w280-h280/hp-15s-fr2515tu-lapt.webp",
        "productName": "HP 15s-fr2515TU Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹38,500",
        "rating": "4.1",
        "specScore": "55",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9x9Wm9Q2C~f~Ji.hrhAgTYBOr3Uh7tBcYuUaTcAs3acYZc55UtcWaucXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54Fcg3o454UCcTrBUshDhDh8a5ZG4bl64XlZPhmBYihkwkp7vSR~jlw..p~ShrhhaFhrhrhhacBrWahrhrBi5G4NOgOAAhrFB5n0b-ur3o43zD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iY77lqqJ6-w280-h280/lenovo-loq-15irh8-82.webp",
        "productName": "Lenovo LOQ 15IRH8 82XV00F5IN 2023 Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹68,890",
        "rating": "4.35",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqEjp6PI5F7X1EphrhArnrysuhyihDRPK50oS0Goh-hrhhaFhrhrhhacBrWahrhrBi5TtP6B2G2hrFB5~N~g2fF3siXo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikNAW1b0d-w280-h280/hp-omen-16-xf0059ax.webp",
        "productName": "HP Omen 16-xf0059AX Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,15,490",
        "rating": "4.25",
        "specScore": "71",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFRQZw1JV8X8XY7ZDUhrhAgTYBOr3Uh7tBcsh2c5bcrnic3IyaucGcsAUrcAs3acGXHPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5bcDgPP4lrDcWrnhNcTrBUshDhDh86a5Ao5aoXGH5rhmBYihkwkp7_0EZV7xRfq7ZhrhhaFhrhrhhacBrWahrhrBi5UABs3A2ihrFB558WYC5JPesW1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izycHE29T-w280-h280/lenovo-loq-2023-gami.webp",
        "productName": "Lenovo LOQ 2023 Gaming Laptop  (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹89,999",
        "rating": "4",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFeET~Nkimdya4_rhrhAgTYBOr3Uh7Taus2scTsNcFUs3ahrhhaFhrhrhhacBrWahrhrBi5yiGutBryhrFB5r_EKZ_uFy1HN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isbIyxTF8-w280-h280/lenovo-thinkbook-14s.webp",
        "productName": "Lenovo ThinkBook 14s Yoga 20WEA00WIH Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win10 Pro)",
        "price": "₹65,999",
        "rating": "4",
        "specScore": "70",
        "features": [
            "11th Gen Intel Core i7 1155G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI1-A6aCzG-rn6uhrhArnrysuhyihDRPlVSbKZXJh-hrhhaFhrhrhhacBrWahrhrBi5YDniQBTBhrFB5nq4SZg2Z589S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2Rnh0zud-w280-h280/dell-alienware-x16-g.webp",
        "productName": "Dell Alienware X16 Gaming Laptop (13th Gen Core i9/ 32GB/ 2TB SSD/ Win 11/ 16GB Graph)",
        "price": "₹4,54,290",
        "rating": "4.35",
        "specScore": "84",
        "features": [
            "13th Gen Intel Core i9 13900HK",
            "14 Cores (6P + 8E), 20 Threads",
            "32 GB LPDDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "16 inches, 3200 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREv_mlOjuJVIrjikuvhrhArnrysuhyihDRPwH.GKo0lh-hrhhaFhrhrhhacBrWahrhrBi5AYA8iB6ThrFB5fsD6Yp1PNC_E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iCquVbIDq-w280-h280/msi-modern-15-b12m-6.webp",
        "productName": "MSI Modern 15 B12M-612IN Laptop (12th Gen Core i3/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹33,990",
        "rating": "4.35",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFqFnw1bwu5gnnbhrhAgTYBOr3Uh7nFYcnsia3uc54cYuUaTcAs3acYZc5oUtcWauc5o54Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac65onscb5oYucUtYucTYWtUcTrBUshDhDh8bPA5HGPlgigZ6hmBYihkwkp7fex7zGpwfx-_hrhhaFhrhrhhacBrWahrhrBi58FH66uFnhrFB5uYkaVnA4PPQ4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5B47RVbd-w280-h280/dell-alienware-m16-g.webp",
        "productName": "Dell Alienware m16 Gaming Laptop (AMD Ryzen 9 7845HX/ 32GB/ 2TB SSD/ Win 11/ 12GB Graph)",
        "price": "₹2,89,990",
        "rating": "4.7",
        "specScore": "91",
        "features": [
            "7th Gen Amd Ryzen 9 7845HX",
            "12 Cores, 24 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GEFORCE RTX 4080",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJUSZRvzJmoYR9xAhrhArnrysuhyihDRPwl5G_ewvh-hrhhaFhrhrhhacBrWahrhrBi5uyroCCGshrFB5U-xwXvCaQ8~5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i27RKWbXL-w280-h280/acer-nitro-16-an16-4.webp",
        "productName": "Acer Nitro 16 ‎AN16-41 2023 Gaming Laptop (AMD Ryzen 7 7840HS/ 8GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹88,990",
        "rating": "4.3",
        "specScore": "72",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIAeqgtmYYYWFd8hrhArnrysuhyihDRPwX5KKKV4h-hrhhaFhrhrhhacBrWahrhrBi5CQXoZ8buhrFB5oSobQ.Vo9Xvf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9ZaO3lWM-w280-h280/asus-vivobook-pro-15.webp",
        "productName": "Asus Vivobook Pro 15 M6500QC-LK742WS Laptop (Ryzen 7 5800H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹75,990",
        "rating": "4.75",
        "specScore": "69",
        "features": [
            "5th Gen AMD Ryzen 7 5800H",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEosn5ZyZzdJnnPhrhAgTYBOr3Uh7rFCFcrnic3IyaucGcsAUrcAs3ac5PUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcu2YiYrc3UDcZP4PcHW6cWii3bcnb4PPNAcTOGHo8FcA3arUs3cTrBUshDhDh8aGXbXAZG4XHZghmBYihkwkp7e.x.Vx_Vxv77hrhhaFhrhrhhacBrWahrhrBi5gFPC4ZTXhrFB5~kJps8RyxnAZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifp2XCblj-w280-h280/walker-nu14a1-laptop.webp",
        "productName": "Walker NU14A1 Laptop (Celeron N4020/ 4GB/ 128GB SSD / Win11 Home)",
        "price": "₹12,990",
        "rating": "4.35",
        "specScore": "33",
        "features": [
            "Intel Celeron  N4020",
            "Dual Core, 2 Threads",
            "4 GB DDR4 RAM",
            "128 GB SSD",
            "Intel Integrated UHD Graphics",
            "14.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UKI5NVO-TdrRYuUhrhArnrysuhyihDRPw70mmJzZh-hrhhaFhrhrhhacBrWahrhrBi5PyYbYDQghrFB5~4Hp-~XWg38V"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIlXYbnIq-w280-h280/dell-inspiron-14-543.webp",
        "productName": "Dell Inspiron 14 5430 2023 Laptop (13th Gen Core i5/ 8GB/ 1TB SSD/ Win11)",
        "price": "₹60,719",
        "rating": "4.3",
        "specScore": "56",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5  RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afrQyRsU9d~PxafVghrhArnrysuhyihDRPKRmx~_e1h-hrhhaFhrhrhhacBrWahrhrBi5O5b8PYBahrFB53gEixjrCZw7p"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixv3hBnMs-w280-h280/infinix-inbook-y1-pl.webp",
        "productName": "Infinix INBook Y1 Plus Neo 2023 XL30 Laptop (Intel Celeron N5100/ 4GB/ 128GB SSD/ Win 11 Home)",
        "price": "₹18,490",
        "rating": "4.15",
        "specScore": "42",
        "features": [
            "11th Gen Intel Celeron N5100",
            "Quad Core, 4 Threads",
            "4 GB LPDDR4X RAM",
            "128 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqP.61GDg~SejS5hrhArnrysuhyihDRPwvb1zKmVh-hrhhaFhrhrhhacBrWahrhrBi5b5Xias23hrFB5Sf8bTNA5uTk1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAKXWZTeG-w280-h280/hp-pavilion-plus-14.webp",
        "productName": "HP Pavilion Plus 14-eh1022TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹80,990",
        "rating": "4.75",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 1340P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2240 x 1400 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xYgN.3pBDuvoNghrhAgTYBOr3Uh7tBcBr2YTh3cBTCFcoPoHcYuUaTcAs3acY4c5ZUtcWauc5ZHPBc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5Hcat5PooUCcUtYucTYWtUcTrBUshDhDh8lZHaHGXAHPGiPhmBYihkwkp7~zxwSjxzGKZShrhhaFhrhrhhacBrWahrhrBi5BAGuQ4UuhrFB5RUD25WK1-aSV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8nfgUd7L-w280-h280/hp-15s-ey2001au-lapt.webp",
        "productName": "HP 15s-ey2001AU Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹47,218",
        "rating": "4.6",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 7   5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqSti5ClZqfumwahrhArnrysuhyihDRPwlKKdo-Rh-hrhhaFhrhrhhacBrWahrhrBi56IlHuBP8hrFB5WTyOBGw~TOlG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQ6sYOXAu-w280-h280/infinix-zerobook-zl5.webp",
        "productName": "Infinix Zerobook ZL513 2023 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹51,990",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzBK8IUj8qG7SJJhrhAgTYBOr3Uh7YugYuYDcya3s6ssOc5ZcYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacyT45ZcUtYucTYWtUcTrBUshDhDh8riGaPobaX6XA4hmBYihkwkp7vx17JG-.7vv_hrhhaFhrhrhhacBrWahrhrBi5gb34HAAPhrFB5vBUJYSdnFFAN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBQPQGtfN-w280-h280/dell-vostro-5620-lap.webp",
        "productName": "Dell Vostro 5620 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹40,390",
        "rating": "4.5",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11  OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYbvmEkv3Droxt6hrhAgTYBOr3Uh7iaTTc2sFU3scYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac4boPcTrBUshDhDh8AAo56HGaA54ZghmBYihkwkp7~~KSKZS7zRpehrhhaFhrhrhhacBrWahrhrBi5g4CBWWgChrFB5-5a415~1X8vt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iS9IkxwdZ-w280-h280/hp-255-g9-840t7pa-la.webp",
        "productName": "HP 255 G9 840T7PA Laptop (AMD Athlon Silver-3050U/ 4GB/ 256GB SSD/ DOS)",
        "price": "₹18,999",
        "rating": "4.25",
        "specScore": "44",
        "features": [
            "3rd Gen AMD Athlon 3050U",
            "Dual Core, 2 Threads",
            "4 GB DDR4 RAM",
            "256 GB SSD",
            "AMD Integrated",
            "15.6 inches, 1366 x 768 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF4pCsSSGdDvVnbhrhAgTYBOr3Uh7tBco44cWlcrnicrUtTsuciCrTcAs3acFYThCcZP4PCcHcW6co4bcW6cFFicisFcUtYucTYWtUcTrBUshDhDh8ggrAXro6obZAohmBYihkwkp7~vVHRVz.V4wwhrhhaFhrhrhhacBrWahrhrBi5AWPu6HNUhrFB5.Y1PbQnOzX0b"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXNydflLG-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82XQ008EIN Laptop (AMD Ryzen 3 7320U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹32,390",
        "rating": "4.7",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon 610M Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JiNeoVSaURwv5.DhrhAgTYBOr3Uh7Taus2scYiarBricrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54rnuXcUtYucTYWtUcTrBUshDhDh86Z4rPbibrZrbZhmBYihkwkp7eoj-SjS._S..hrhhaFhrhrhhacBrWahrhrBi5tYZPbrrbhrFB51KtIZFaEguI_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i71dKhQGT-w280-h280/dell-inspiron-5620-i.webp",
        "productName": "Dell Inspiron 5620 ICC-C783531WIN8 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 2GB Graph)",
        "price": "₹67,500",
        "rating": "4.65",
        "specScore": "69",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "2 GB NVIDIA GeForce MX570",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI~Zf~OYC1NOX6KhrhArnrysuhyihDRPRSfvXpV~h-hrhhaFhrhrhhacBrWahrhrBi5WAtC2GuahrFB5oil~ytHsvqGw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWe7K0YKV-w280-h280/lenovo-v15-g3-iap-82.webp",
        "productName": "Lenovo V15 G3 IAP 82TTA00UIH Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹31,790",
        "rating": "4.7",
        "specScore": "50",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY5X3~pnkO-NbHRhrhAgTYBOr3Uh7Taus2sc254cYuUaTcAs3acYZc5oUtcWaucXcW6c45ocW6cFFicisFc45ocn6cW3rBtYAFcTrBUshDhDh8ig4iGlXoZoGgbhmBYihkwkp71XflqRj._fxVhrhhaFhrhrhhacBrWahrhrBi5iDoCggyghrFB5HBeekgojlXXX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ife6lfAm6-w280-h280/lenovo-v15-g3-laptop.webp",
        "productName": "Lenovo V15 G3 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/Win11)",
        "price": "₹43,990",
        "rating": "4.6",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwrkfKWvW7qDKWIhrhArnrysuhyihDRPwbf5V7f7h-hrhhaFhrhrhhacBrWahrhrBi5iYAIingrhrFB5D73G5EmakZJG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifn0jg9a5-w280-h280/dell-inspiron-15-353.webp",
        "productName": "Dell Inspiron 15 3530 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,861",
        "rating": "4.15",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i3 1305U",
            "5 Cores (1P + 4E), 6 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xC0QrA1PK9nnpdhrhArnrysuhyihDRPKRmmfR.fh-hrhhaFhrhrhhacBrWahrhrBi5CnyYY4oihrFB57T2gYdy7HlN3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixrS2go2p-w280-h280/infinix-inbook-x2-sl.webp",
        "productName": "Infinix INBook X2 Slim Series XL23 Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹36,990",
        "rating": "4.55",
        "specScore": "54",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzgtIepsxDqzJNWhrhAgTYBOr3Uh7YugYuYDcDocFTYncYuUaTcAs3acY4c55UtcWauc5544WGc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacDToZcUtYucTYWtUcTrBUshDhDh8A4bHZZb6HPg6ahmBYihkwkp71EHG.efeZxw_hrhhaFhrhrhhacBrWahrhrBi5GYr884YDhrFB5l2P1bS-C3opg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijoL1uHmJ-w280-h280/dell-inspiron-5430-i.webp",
        "productName": "Dell Inspiron 5430 IN54308TR2G001ORS1 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹62,719",
        "rating": "4.1",
        "specScore": "48",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67Glzn7k_qPdy3yhrhArnrysuhyihDRPKRmxo1Zbh-hrhhaFhrhrhhacBrWahrhrBi5yXsYO6CihrFB5vbC19OJKD7m8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i60sAZJNM-w280-h280/dell-inspiron-5430-i.webp",
        "productName": "Dell Inspiron 5430 IN5430YXVW9M01ORS1 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹54,999",
        "rating": "4.55",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gxy2~87~mdPjaPhrhAA3snrh7iaTTcYuFBY3suc4HZPcYuUaTcAs3acY4c5ZUtcWauc5HcYuAtcXW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5cYuUaTcY3YFcDacgCTTcticBTCFciYFBTrIcBTrUYuCncFYThCcYu4HZPID28lnP5s3F5ch-hDoGHPGohrhhaFhrhrhhacBrWahrhrBi5AtiQPTYshrFB5FdJtxQv_w-Z4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iiqJrGsWP-w280-h280/acer-one-14-z8-415un.webp",
        "productName": "Acer One 14 Z8-415UN.599SI.009 Laptop (11th Gen Core i3 / 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹25,990",
        "rating": "4.45",
        "specScore": "53",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "‎Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz.pan5qzbiD5QehrhAgTYBOr3Uh7rAa3chFcoPoHcYuUaTcAs3acYZc55UtcWauc5554WHcXcW6co4bcW6cFFic8Yuis8Fc55ctsnac5HcyXcH54cUtYucTYWtUcTrBUshDhDh8l56rAb6r4GoH4hmBYihkwkp71x4wlX7xXxqShrhhaFhrhrhhacBrWahrhrBi5aXbGsPXyhrFB5KP607TpHo8Bl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icCy4H6mZ-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1502ZA-EJ542WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹51,389",
        "rating": "4.55",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FISkURseUygmYp~hrhArnrysuhyihDRPKl-KRwwvh-hrhhaFhrhrhhacBrWahrhrBi5XTb5Yry2hrFB50wpkFzx6spOa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLETCurLF-w280-h280/asus-zenbook-14x-ole.webp",
        "productName": "Asus Zenbook 14X OLED 2023 UM5401QA-KM751WS Laptop (Ryzen 7 5800HS / 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹69,990",
        "rating": "4.3",
        "specScore": "61",
        "features": [
            "5th Gen AMD Ryzen 7 5800HS",
            "Octa Core, 16 Threads",
            "16 GB LPDDR4X RAM",
            "1 TB SSD",
            "AMD Radeon AMD",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzIQ201_A0PZowphrhAgTYBOr3Uh7rFCFcyau6ssOc5HDcsTaicrnic3IyaucGcsAUrcAs3ac4XPPtFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacCn4HP5NrcOnG458FcUtYucTYWtUcTrBUshDhDh844b6gbHogHi4XhmBYihkwkp7.VS~R0.JSp1GhrhhaFhrhrhhacBrWahrhrBi5oAoHTa5yhrFB5vobCVoz_jI5K"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isuTscTUn-w280-h280/dell-g15-5530-gn5530.webp",
        "productName": "Dell G15-5530 GN5530D83M6002ORB1 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹74,990",
        "rating": "4.1",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2GvnxyTK3AaSdRrhrhAA3snrh7iaTTcW54c44ZPcYuUaTcAs3acY4c5ZUtcWaucWrnhNcTrBUsBc8YUtc3W6cOaI6sr3ic5bW6c45oW6cFFic8Yuis8Fc55cbW6cW3rBtYAFc54cbcYuAtc5oPctycgticiYFBTrIcnFcsggYAacoPo5cir3OcFtris8cW3rIcoclGcOWch-hDoGZZPlhrhhaFhrhrhhacBrWahrhrBi5nlF4yUZAhrFB5QtbxlUw.fw~w"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF3Q2gB2B-w280-h280/dell-g15-5530-gn5530.webp",
        "productName": "Dell G15-5530 GN5530VMMD9002ORB1 Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹90,719",
        "rating": "4.1",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afrO73EvGAIKUksluhrhArnrysuhyihDRPKRm-KZvvh-hrhhaFhrhrhhacBrWahrhrBi5tCgyNTB2hrFB5IwA.ROU.tC4H"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDuwdlvMt-w280-h280/asus-vivobook-15x-20.webp",
        "productName": "Asus Vivobook 15X 2023 K3504VAB-NJ321WS Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹38,990",
        "rating": "4.65",
        "specScore": "52",
        "features": [
            "13th Gen ‎Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gb5Q8SJF~iZpnshrhAA3snrh7rFCFc2Y2s6ssOc54DcOZ4PH2r6cuQZoo8FcYuUaTcAs3acYZc5ZUtcWaucUtYuchYcTYWtUcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticTaic6huTYUciYFBTrIcnFcsggYAacoPo5cAssTcFYThCc5cbcOWch-hDoG45ZohrhhaFhrhrhhacBrWahrhrBi54ygAoaaYhrFB56fA6IfVf4QTb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijbCSdqUR-w280-h280/hp-pavilion-x360-14.webp",
        "productName": "HP Pavilion x360 14-ek1020TU Laptop (13th Gen Core i7/ 16GB/ 512 GB SSD/ Win11)",
        "price": "₹88,800",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqg2-_4~VQOTy2FhrhArnrysuhyihDRPwRRvzew.h-hrhhaFhrhrhhacBrWahrhrBi5iN5ZuQrOhrFB55UTrPIzO2r~Y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0zippBmi-w280-h280/asus-rog-strix-g16-2.webp",
        "productName": "Asus ROG Strix G16 2023 G614JV-N4141WS Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,59,990",
        "rating": "4.35",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i9 13980HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFRQXffEnrYK-dmmXxhrhAgTYBOr3Uh7rFCFc3sWcFU3YDcW5bcoPoZclP8t3c6rUhUIcYuUaTctDcFa3YaFcAs3acYlc5ZUtcWauc5ZlXPtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPcoHPctyc5HPcUWBcWb5HQ2cuH5H58FcWrnhNcTrBUshDhDh86o65GZl4GX4GGhmBYihkwkp71x1wpl77l~SfhrhhaFhrhrhhacBrWahrhrBi582HyA5n2hrFB5GkuIKZb2ffqx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iddNWcUSU-w280-h280/asus-tuf-f15-fx506hf.webp",
        "productName": "Asus TUF F15 FX506HF-HN024W Gaming Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹51,990",
        "rating": "4.7",
        "specScore": "64",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3RbuRrZQ-r3aRzhrhAA3snrh7rFCFcUCgcWrnhNcg54cgD4PbtgctuPoH8FcYuUaTcAs3acY4c55UtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55cHW6cWii3bc54cbcYuAtcgticYBFciYFBTrIcnFcsggYAacoPo5cW3rBthschncocZOWch-hDoGo4G4hrhhaFhrhrhhacBrWahrhrBi5asZF8CY6hrFB5O-Wtm3w-6Sil"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNUsDarcz-w280-h280/hp-15-fd0013tu-lapto.webp",
        "productName": "HP 15-fd0013TU Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹56,799",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G7BuGyuHNBgx~ahrhAA3snrh7tBc54cgiPP5ZUCcYuUaTcAs3acY4c5ZUtcWauc54cbcYuAtc5bW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcY3YFcDacgticiYFBTrIcurUC3rTcFYThCcGBGP4Brch-hDoG45b4hrhhaFhrhrhhacBrWahrhrBi5y2iZOgsOhrFB52wxnkyb_t1fy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHDoDXknd-w280-h280/hp-15s-fr4001tu-lapt.webp",
        "productName": "HP 15s-fr4001TU Laptop (11th Gen Core i5/16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,490",
        "rating": "4.15",
        "specScore": "60",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF1XXemuYPvSIUPhrhAgTYBOr3Uh7tBcoPoHcYuUaTcAs3acY4c55UtcWauc5544WGc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54Fcg3HPP5UCcUtYucTYWtUcTrBUshDhDh866bH6bg5bbGi4hmBYihkwkp7.deRb7w-0E1_hrhhaFhrhrhhacBrWahrhrBi5QIrb23tIhrFB5-o7zjdoaGD3K"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijViMd3jW-w280-h280/acer-one-14-z8-415-l.webp",
        "productName": "Acer One 14 Z8-415 Laptop (11th Gen Core i5 / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,999",
        "rating": "4.1",
        "specScore": "53",
        "features": [
            "11th Gen Intel Core i5  1135G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "‎Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzgY4rTmNBZ5BJJhrhAgTYBOr3Uh7rAa3chF5HcoPoHc6huTYUcYuUaTcAs3acY4c55UtcWauc5544WGcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacyXcH54cUtYucTYWtUcTrBUshDhDh8glAa4glXX4Po6hmBYihkwkp7~qRpK-KzVqVdhrhhaFhrhrhhacBrWahrhrBi5buUsGlOFhrFB5wUS32UDA4t-8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqQ76ZiIa-w280-h280/hp-15s-fy5002tu-lapt.webp",
        "productName": "HP 15s-fy5002TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹48,990",
        "rating": "4.1",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFdozKtyHQniS2khrhAgTYBOr3Uh7tBcoPoZc6huTYUcYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgI4PPoUCcUtYucTYWtUcTrBUshDhDh8lPHbarg4rHrglhmBYihkwkp7.deReG.l4lqJhrhhaFhrhrhhacBrWahrhrBi5GCQAtTCghrFB5UyEOpnto6d0p"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNJI8BAVo-w280-h280/hp-15-fc0030au-lapto.webp",
        "productName": "HP 15-fc0030AU Laptop (AMD Ryzen 5 7520U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹43,999",
        "rating": "4.4",
        "specScore": "51",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gla6OrWiEnzgJnhrhAA3snrh7tBc54cgAPPZPrCcrnic3Iyauc4c54cbcYuAtc5bW6c45oW6c8Yuis8Fc55cnFcsggYAacoPo5crnic3riasucgticYBFciYFBTrIcurUC3rTcFYThCcGTPZHBrch-hDoGZZoXhrhhaFhrhrhhacBrWahrhrBi55PH8QrynhrFB5Kkoop4pBwWbb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieDL9Di5R-w280-h280/hp-15-fd0006tu-lapto.webp",
        "productName": "HP 15-fd0006TU Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,490",
        "rating": "4.1",
        "specScore": "46",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiC3Hrg.RjK3vD4EShrhAA3snrh7tBc54cgiPPPbUCcYuUaTcAs3acYZc5ZUtcWauc54cbcYuAtcXW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcCticgticiYFBTrIcurUC3rTcFYThCcGBbyXBrch-hDoG4GGGhrhhaFhrhrhhacBrWahrhrBi5IFbUBPWChrFB5esErdBRt8DKH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ij4kp1I8t-w280-h280/realme-book-prime-cl.webp",
        "productName": "Realme Book Prime CloudPro002 Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹43,790",
        "rating": "4.5",
        "specScore": "56",
        "features": [
            "11th Gen Intel Core i5 11320H",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2160 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIwffXl41EsqVaPhrhArnrysuhyihDRPK57ZwJbxh-hrhhaFhrhrhhacBrWahrhrBi5DA8oCAGQhrFB5egEPu53k5o~m"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZIyLsbtA-w280-h280/hp-15-fd0011tu-lapto.webp",
        "productName": "HP 15-fd0011TU Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹53,900",
        "rating": "4.05",
        "specScore": "50",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afryIxaWa3ye99eWUhrhArnrysuhyihDRPwZvw1G5Gh-hrhhaFhrhrhhacBrWahrhrBi5DZZtIQF3hrFB5lCwCleQrgJbq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i30x39w0C-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 PHN16-71 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,04,990",
        "rating": "4",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB7Hz-pXm9pWldklhrhArnrysuhyihDRPRfd4pfXoh-hrhhaFhrhrhhacBrWahrhrBi5uOYY5bO8hrFB5QIjTYzrdzosS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRlb5mdiu-w280-h280/msi-thin-gf63-12vf-2.webp",
        "productName": "MSI Thin GF63 12VF-268IN Laptop (12th Gen Core i5/ 16GB/ 1TB 256GB SSD/ Win11/ 8GB Graph)",
        "price": "₹95,990",
        "rating": "4",
        "specScore": "72",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB Hard Disk",
            "256 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYApUBkYzVkV5IUhrhAgTYBOr3Uh7nFYcWgbZcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c5cU6ctiico4bcW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5HHctycUtYuc5o2gcobXYucWrnhNcTrBUshDhDh8lHHPla4PPZZ4lhmBYihkwkp7.4xZHKSdKSSxhrhhaFhrhrhhacBrWahrhrBi5UHYOB2WQhrFB5WQb2_xfTy7y3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLsILwCSC-w280-h280/msi-cyborg-15-a12ucx.webp",
        "productName": "MSI Cyborg 15 A12UCX-265IN Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹55,999",
        "rating": "4.1",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Nvidia GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI-~kTZlD5Fz-jIhrhArnrysuhyihDRPwZ-opS7lh-hrhhaFhrhrhhacBrWahrhrBi53233iTu5hrFB59r92G~NWC7OV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imhDqYOKq-w280-h280/asus-vivobook-14x-ol.webp",
        "productName": "Asus Vivobook 14X OLED 2023 K3405VFB-KM541WS Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11/4 GB Graphics)",
        "price": "₹75,990",
        "rating": "4.55",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqfQe2A9WXy0zIthrhArnrysuhyihDRPKXJXX1K7h-hrhhaFhrhrhhacBrWahrhrBi54WCOntPohrFB5IOUOtKYOjk_J"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAJCVM97x-w280-h280/hp-15-fc0026au-lapto.webp",
        "productName": "HP 15-fc0026AU Laptop (AMD Ryzen 3 7320U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹33,460",
        "rating": "4.05",
        "specScore": "50",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xBNX0q7mk_IjD.hrhArnrysuhyihDRPwZvwvHVGh-hrhhaFhrhrhhacBrWahrhrBi5tFniZroDhrFB5JAwRbX~geQOP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ig5tK2dFn-w280-h280/hp-victus-16-d0333tx.webp",
        "productName": "HP Victus 16-d0333TX Gaming Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹58,990",
        "rating": "4.65",
        "specScore": "70",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzFk6BZDBa1J_4XhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c55UtcWauc55HPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3AacWUDc5b4Pc5bciPZZZUDcWrnhNcTrBUshDhDh85XZGg5Ggrl6lAhmBYihkwkp7.deR1qqfdl7dhrhhaFhrhrhhacBrWahrhrBi56lDHby6FhrFB57XnQKgFQJykv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGV5yy3hY-w280-h280/asus-vivobook-14-202.webp",
        "productName": "Asus VivoBook 14 2023 X1404VA-NK321WS Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹35,990",
        "rating": "4.65",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYZ5fQOKpUbBJVihrhAgTYBOr3Uh7rFCFc2Y2s6ssOc5HcoPoZcYuUaTcAs3acYZc5ZUtcWauc5Z54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacD5HPH2rcuOZoo8FcUtYucTYWtUcTrBUshDhDh8HlAPH4PilaalihmBYihkwkp7.K~-ZEVfqdfvhrhhaFhrhrhhacBrWahrhrBi56QGtHIs2hrFB56X~9ab4-BTKz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSKYtrRrg-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2023 X1504VA-NJ324WS Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹38,990",
        "rating": "4.25",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqwJ3okn~RsF46_hrhArnrysuhyihDRPRvf5lVGvh-hrhhaFhrhrhhacBrWahrhrBi5IQQtH3IrhrFB5yPFR3b6Z~GzW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwO3TvRXD-w280-h280/asus-vivobook-14-202.webp",
        "productName": "Asus VivoBook 14 2023 X1404VA-NK522WS Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹47,990",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYlsIxBA~0QDTDdhrhAgTYBOr3Uh7rFCFc2Y2s6ssOc5HcoPoZcYuUaTcAs3acY4c5ZUtcWauc5ZZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacD5HPH2rcuO4oo8FcUtYucTYWtUcTrBUshDhDh856XXXAoXogGgghmBYihkwkp7.K~-fxx7.z07hrhhaFhrhrhhacBrWahrhrBi5AbOZGBs8hrFB5_-E5O6iD-VY."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2p8i72Rd-w280-h280/hp-255-g9-7b1l8pa-la.webp",
        "productName": "HP 255 G9 7B1L8PA Laptop (AMD Ryzen 5 5625U/ 8GB/ 512 GB SSD/ Win11 Home)",
        "price": "₹32,499",
        "rating": "4",
        "specScore": "60",
        "features": [
            "5th Gen AMD Ryzen 5 5625U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrziYC-OQZGVwTCEhrhAgTYBOr3Uh7tBco44cWlcFYThCcrnic3Iyauc4ctaDrcAs3ac3Iyau4c4bo4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac6CFYuaFFcTrBUshDhDh8465Xa55ioagP6hmBYihkwkp7.vXfH~7Zxd-0hrhhaFhrhrhhacBrWahrhrBi5TAF2ZCP6hrFB5dKyEesaFkfHU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZFhUtHYn-w280-h280/lenovo-v15-g2-ijl-8.webp",
        "productName": "‎Lenovo V15 G2 IJL 82QYA00HIN Laptop (Celeron N4500/ 8GB/ 256GB SSD/ DOS)",
        "price": "₹21,399",
        "rating": "4.35",
        "specScore": "38",
        "features": [
            "Intel Celeron  N4500",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty",
            "1 USB 3.0 Ports"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqZ7GfOk8~odOFThrhArnrysuhyihDRPwoX7~Zfmh-hrhhaFhrhrhhacBrWahrhrBi5Xbb83P2thrFB5XO_RYjHKS6k3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iR5axHlKS-w280-h280/apple-macbook-air-15.webp",
        "productName": "Apple MacBook Air 15 2023 Laptop (Apple M2/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹1,01,990",
        "rating": "4.55",
        "specScore": "52",
        "features": [
            "Apple M2",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "10-Core GPU",
            "15.3 inches, 2880 x 1864 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFw~uqTJoAFbFbkuTkhrhAgTYBOr3Uh7rBBTacnrA6ssOcrY3coPoZcnocXcW6co4bcW6cFFicnrAsFc2auUC3rcnNO8Ztucrh-hDh8ZgAHAPlZlZZlrhmBYihkwkp7~jo0dqvp-pKKhrhhaFhrhrhhacBrWahrhrBi53CtB3t5ChrFB5n82QRr_268dV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itU0fxxZ0-w280-h280/hp-spectre-x360-16-f.webp",
        "productName": "HP Spectre x360 16-f2005TX Laptop (13th Gen Core i7/ 32GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹1,59,999",
        "rating": "4.05",
        "specScore": "84",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "32 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB  Intel Arc A370M Graphics",
            "16 inches, 3840 x 2400 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_XmHT4ydOA8.AF_hrhArnrysuhyihDRPw5wmpmJ_h-hrhhaFhrhrhhacBrWahrhrBi5iT4YuGF8hrFB5pgGe6yAwEb7_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ie14cSoYp-w280-h280/infinix-inbook-y1-pl.webp",
        "productName": "Infinix INBook Y1 Plus Neo XL30 Laptop (Intel Celeron N5100/ 8GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹22,990",
        "rating": "4.2",
        "specScore": "47",
        "features": [
            "11th Gen Intel Celeron N5100",
            "Quad Core, 4 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ6_bF_28AmFOzZhrhAgTYBOr3Uh7YugYuYDcI5cBTCFcuascYuUaTcAaTa3sucNCricAs3ac55UtcWaucQFTcu45PPcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacDTZPcUtYucTYWtUcTrBUshDhDh85XAHliaPaaaZihmBYihkwkp7.GfwJSz1x0ffhrhhaFhrhrhhacBrWahrhrBi5O4t4iQCrhrFB5Vmyn82anYov1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inhj5vKqF-w280-h280/honor-magicbook-x16.webp",
        "productName": "Honor MagicBook X16 2023 ‎‎‎BRN-F58 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹42,529",
        "rating": "4.55",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw.nT~dFb6Ji90ShrhArnrysuhyihDRPRfVXzpf-h-hrhhaFhrhrhhacBrWahrhrBi5IBW2WOyyhrFB5dZ.uEkNp7Ufk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3dBJM51I-w280-h280/lenovo-v15-g3-82tta0.webp",
        "productName": "Lenovo V15 G3 82TTA00VIH Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/Win11)",
        "price": "₹32,099",
        "rating": "4.15",
        "specScore": "50",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFqGmAjxowPG~UWhrhAgTYBOr3Uh7Taus2sc254cYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacWZcYrBcUtYucTYWtUcTrBUshDhDh8gb5GoHlla5Ab4hmBYihkwkp7.Ze1~SzEdvV7hrhhaFhrhrhhacBrWahrhrBi5nOnnb3A4hrFB5uCVB.~jyKpXX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iINoQoprE-w280-h280/hp-15-fc0028au-lapto.webp",
        "productName": "HP 15-fc0028AU Laptop (AMD Ryzen 5 7520U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹39,700",
        "rating": "4.7",
        "specScore": "48",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xFaRiwdIOgVPfVhrhArnrysuhyihDRPR.fz11.xh-hrhhaFhrhrhhacBrWahrhrBi5tO3Ya4I4hrFB5rHCs-5VwtGzS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijH5CUlUH-w280-h280/hp-14s-dy5008tu-lapt.webp",
        "productName": "HP 14s-dy5008TU Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.6",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqRAgp2GFiQarr0hrhArnrysuhyihDRPR.eXXf1zh-hrhhaFhrhrhhacBrWahrhrBi5XQQUC8GohrFB5YF~zP2qXzHyy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2DXLpJRv-w280-h280/msi-modern-14-c12m-4.webp",
        "productName": "MSI Modern 14 C12M-440IN Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.35",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF7xZtAr5Gl0o9ahrhAgTYBOr3Uh7nFYcnsia3uc5HcYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacA5oncHHPYucA5onsc5Po5YucUtYucTYWtUcTrBUshDhDh8Z4Pooo5ZXib66hmBYihkwkp7p0b0-7f0R.ephrhhaFhrhrhhacBrWahrhrBi52AFagFN6hrFB5UrkiDmuZzvV0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPS55GBzo-w280-h280/msi-modern-14-c11m-0.webp",
        "productName": "MSI Modern 14 C11M-030IN Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹59,990",
        "rating": "4.4",
        "specScore": "53",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzFNtauub~eXSrahrhAgTYBOr3Uh7nFYcnsia3uc5HcYuUaTcAs3acY4c55UtcWauc5544WGcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacA55ncPZPYucUtYucTYWtUcTrBUshDhDh86GZll5io5lHrbhmBYihkwkp7p0b077eHvSKXhrhhaFhrhrhhacBrWahrhrBi5Qb2i2ArQhrFB5NiUdtp19qE9Z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQ2jNAWsV-w280-h280/asus-vivobook-go-14.webp",
        "productName": "Asus Vivobook Go 14 2023 E1404FA-NK322WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹29,999",
        "rating": "4.65",
        "specScore": "50",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JU3zSyxuspeTHjPhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc5HcoPoZcrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca5HPHgrcuOZo58FcUtYucTYWtUcTrBUshDhDh8A4gXA6Xa4oAZZhmBYihkwkp7eSe4feV-G7~1hrhhaFhrhrhhacBrWahrhrBi5BXBuy5r8hrFB5QEKAzjJpgb9y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOsDnXOY0-w280-h280/msi-modern-14-c12m-4.webp",
        "productName": "MSI Modern 14 C12M-445IN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹29,990",
        "rating": "4.25",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQatTYYYNoalP5ghrhAgTYBOr3Uh7nFYcnsia3uc5HcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacA5oncHH4YucA5onsc5PooYucUtYucTYWtUcTrBUshDhDh86Xl6PlHZHbi54hmBYihkwkp7p0b0~1d17wRJhrhhaFhrhrhhacBrWahrhrBi5Q8YBGiOGhrFB5q3PT0ml5pKXA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwJJdtxHB-w280-h280/hp-chromebook-15a-na.webp",
        "productName": "HP Chromebook 15a-na0008TU Laptop (Intel Celeron N4500/ 4GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹18,990",
        "rating": "4.45",
        "specScore": "33",
        "features": [
            "Intel Celeron  N4500",
            "Dual Core, 2 Threads",
            "4 GB LPDDR4x RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1366 x 768 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqPO1mRSk5BB3.PhrhArnrysuhyihDRPRfzZzXReh-hrhhaFhrhrhhacBrWahrhrBi5WG3nDbUohrFB5dT-50Xfl.IZp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7ZSnyKNa-w280-h280/msi-modern-14-c11m-0.webp",
        "productName": "MSI Modern 14 C11M-031IN Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹28,990",
        "rating": "4.15",
        "specScore": "54",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIZbUroNA7fPPwfhrhArnrysuhyihDRPR~Re-b.zh-hrhhaFhrhrhhacBrWahrhrBi5NZD3nlu3hrFB5BjYCEfNRiS3m"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ineazEZT8-w280-h280/asus-vivobook-pro-15.webp",
        "productName": "Asus Vivobook Pro 15 M6500QC-HN542WS Laptop (Ryzen 5 5600H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹58,100",
        "rating": "4.1",
        "specScore": "65",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xEVlZGRjE1lRkKhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcB3sc54cA3arUs3crnic3Iyauc4ctaDrcAs3ac4bPPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5HHctyc4PcUWBcnb4PPNActu4Ho8FcWrnhNcTrBUshDhDh85546HPGrZirGbhmBYihkwkp7d1l1jvbGwpGxhrhhaFhrhrhhacBrWahrhrBi5UuWY4PZChrFB58XTapx5jJN5~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXwN4qHyM-w280-h280/lenovo-yoga-slim-7-p.webp",
        "productName": "Lenovo Yoga Slim 7 ProX 82TK00AFIN Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 4GB Graphics)",
        "price": "₹1,24,990",
        "rating": "4.55",
        "specScore": "75",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "14.5 inches, 3072 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB9_iG9yZ-PA4RU7hrhArnrysuhyihDRPRvHwxzz_h-hrhhaFhrhrhhacBrWahrhrBi5PQANPAUthrFB5kA~AWtUd8GOB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy67kSPjj-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 2023 E1504FA-NJ323WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹33,600",
        "rating": "4.25",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqjX1X210eR6~1mhrhArnrysuhyihDRPRzJKvV75h-hrhhaFhrhrhhacBrWahrhrBi5nPsXX6WOhrFB5CbFyo9QBAn04"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuZk3XOoU-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 2023 E1504FA-NJ543WS Laptop (Ryzen 5 7520U / 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹42,239",
        "rating": "4",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqxv07kizIWAK0thrhArnrysuhyihDRPR~eS455wh-hrhhaFhrhrhhacBrWahrhrBi5tNuCZInXhrFB5kFH-_AI04zi1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSY8nHKx9-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 2023 E1504FA-NJ522WS Laptop (Ryzen 5 7520U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹38,990",
        "rating": "4.5",
        "specScore": "54",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQOXUQra4mlePG3hrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54coPoZcrnic3Iyauc4cNCricAs3acG4oPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcuQ4o58FcUtYucTYWtUcTrBUshDhDh8H4H656ZGi6aXlhmBYihkwkp7dvdEVvpp_d.~hrhhaFhrhrhhacBrWahrhrBi5guIu63T5hrFB5JFH4jOSz6Psy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icamBJvEM-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 OLED 2023 E1504FA-LK322WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzYFi9_6ldJQn19hrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54csTaicoPoHcrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcTOZoZ8FcUtYucTYWtUcTrBUshDhDh84iXZ5ZGbbgAbghmBYihkwkp7p7_x7xG.zVSxhrhhaFhrhrhhacBrWahrhrBi5bFylOX6rhrFB5rRKbJoDqv~fA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZUJPXTx7-w280-h280/msi-katana-17-b13udx.webp",
        "productName": "MSI Katana 17 B13UDXK-255IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹94,389",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqQNutKXHvsr8.DhrhArnrysuhyihDRPRzJ5vwJ.h-hrhhaFhrhrhhacBrWahrhrBi5bC6BF3iBhrFB5lBKaIekK~IS."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igeKwE3uE-w280-h280/dell-inspiron-15-352.webp",
        "productName": "Dell Inspiron 15 3520 D560915WIN9S Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,990",
        "rating": "4.45",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFxVFoX2z.HS_SAhrhAgTYBOr3Uh7iaTTcYuFBY3sucZ4oPcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacua8c54cTrBUsBcUtYucTYWtUh-hDh8oibaa5XPHGHXghmBYihkwkp7-G4S-7xK-b-dhrhhaFhrhrhhacBrWahrhrBi5rCZY3O5ihrFB5uCvlBfpaVfm4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6vI2Dy7k-w280-h280/primebook-4g-android.webp",
        "productName": "Primebook 4G Android Laptop (MediaTek MT8788/ 4GB/ 64GB eMMC/ Android 11)",
        "price": "₹14,990",
        "rating": "4.75",
        "specScore": "25",
        "features": [
            "MediaTek MTK8788",
            "Octa Core",
            "4 GB LPDDR4 RAM",
            "64 GB Hard Disk",
            "ARM Mali G72",
            "11.6 inches, 1366 x 768 pixels",
            "Android 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzz5m4gaW7Z~JAqhrhAgTYBOr3Uh7B3Yna6ssOcHWchY3sYic6rFaicnaiYrUaOcnUXGXXcHcW6cbHcW6cannAcFUs3rWacB3YnacsFcUtYucTYWtUcTrBUshDhDh8giZrZ54gAa5i4hmBYihkwkp7SodVf0.w0_jJhrhhaFhrhrhhacBrWahrhrBi5uPaa8rWrhrFB5N1tR8V45PUqa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwSj97kY4-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 3 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹69,990",
        "rating": "4.75",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25203%2520Laptop%2520(13th%2520Gen%2520Core%2520i5%252F%25208GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyb3LXVRo-w280-h280/hp-15s-eq2212au-lapt.webp",
        "productName": "HP 15s- eq2212AU Laptop (AMD Ryzen 3 5300U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹30,390",
        "rating": "4",
        "specScore": "53",
        "features": [
            "5th Gen AMD Ryzen 3  5300U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6xseR2NQEy_X1kChrhArnrysuhyihDRPR~doS0Hbh-hrhhaFhrhrhhacBrWahrhrBi5PAF3liiIhrFB5so6QPnztaf~E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixlZKisKj-w280-h280/dell-vostro-3420-lap.webp",
        "productName": "Dell Vostro 3420 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,990",
        "rating": "4",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90VfNSJbA_HZ7bVhrhAgTYBOr3Uh7iaTTc2sFU3scZHoPcYuUaTcAs3acYZc5oUtcWaucXcW6c45ocW6cFFic8Yuis8Fc55ctsnaci44oZoG8YulFcTrBUshDhDh85X6Hio64P4oGrhmBYihkwkp7dbx7w~H~V0oKhrhhaFhrhrhhacBrWahrhrBi5a5inaiWnhrFB5Roswbj-dK65."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i68Sc9Fri-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2022 X1502ZA-EJ515WS Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹44,990",
        "rating": "4.2",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO90~eHXG3X66IPYohrhAgTYBOr3Uh7rFCFc2Y2s6ssOc54cYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacD54PoyrcaQ4548FcUtYucTYWtUcTrBUshDhDh84ooaigGigbX4XhmBYihkwkp7.K.e0RR.jVZ.hrhhaFhrhrhhacBrWahrhrBi5WuFAAZUihrFB53s2EHJztSwJp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iylvexWIX-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 9 QEZ-00065 Laptop (12th Gen Core i5/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹94,990",
        "rating": "4.65",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB SSD",
            "Intel Iris Xe Graphics",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af671sFSY2miDJbg9hrhArnrysuhyihDRPRmf.0KdHh-hrhhaFhrhrhhacBrWahrhrBi5DrHAurNDhrFB58bYbXk9nTT-_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iv8Jwpyar-w280-h280/lenovo-ideapad-flex.webp",
        "productName": "Lenovo IdeaPad Flex 5 82R90068IN Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.5",
        "specScore": "69",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz8zeVY17AuPSanhrhAgTYBOr3Uh7Taus2scYiarBricgTaDc4crnic3IyaucGcsAUrcAs3ac4GPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HrTAGcoc5cTrBUshDhDh8Zo4HGGi5bHGlPhmBYihkwkp7SjlvS7V0Vx.KhrhhaFhrhrhhacBrWahrhrBi53QNZUZrXhrFB5rmjF~sPe~YsX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHKD1sf2i-w280-h280/lenovo-v15-82kda01bi.webp",
        "productName": "Lenovo V15 82KDA01BIH Laptop (AMD Ryzen 3 5300U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹28,990",
        "rating": "4.35",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 3 5300U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzrY8SqYS~TnS7PhrhAgTYBOr3Uh7Taus2sc254crnic3IyaucZcNCricAs3ac4ZPPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacWocrTAcUtYucTYWtUcTrBUshDhDh8gAAaGai6ZP6XGhmBYihkwkp7.Ze104S-eGlRhrhhaFhrhrhhacBrWahrhrBi5TauulFtthrFB5_3KNzdsGZTPG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0u2NYD8W-w280-h280/acer-one-14-z2-493-l.webp",
        "productName": "Acer One 14 Z2-493 Laptop (AMD Ryzen 3 3250U/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹23,990",
        "rating": "4.7",
        "specScore": "47",
        "features": [
            "3rd Gen AMD Ryzen 3  3250U",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ6ywYSTKkkEEI.hrhAgTYBOr3Uh7rAa3chFc5Hcrnic3IyaucZciCrTcAs3acZo4PCcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacyocHlZcUtYucTYWtUcTrBUshDhDh8iPoZPiZPiba4ZhmBYihkwkp7xSp-xSqKzKKHhrhhaFhrhrhhacBrWahrhrBi56ubriIUOhrFB54w3PF5tTu1OW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF9DZFPDC-w280-h280/acer-aspire-3-a315-5.webp",
        "productName": "Acer Aspire 3 A315-59 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹31,990",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afryTrJ4bTloYvdqmhrhArnrysuhyihDRPRbx4JGJmh-hrhhaFhrhrhhacBrWahrhrBi5BTTAbrTGhrFB5HECEOU~osti8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iftciwhPW-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 82K201Y9IN Laptop (AMD Ryzen 5-5600H/ 8GB/ 1TB 256GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹47,990",
        "rating": "4.25",
        "specScore": "65",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "256 GB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQBr5Oe.ViaTPqZhrhAgTYBOr3Uh7Taus2scYiarBricWrnhNcZcrnic3Iyauc4ctaDrcAs3ac4UtcWauc4bPPtcXcW6c5cU6ctiico4bcW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3AacWUDc5b4Pc5oPctycXoOoP5IlYucTrBUshDhDh8HPGrlPiXH65ibhmBYihkwkp7SjK47Hf-S.7.hrhhaFhrhrhhacBrWahrhrBi5yZ6Pu4WghrFB5J1KUuP4Ae8IX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDeaEnMek-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 82SF008YIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹58,491",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JaHyKs9ugz8sEs_hrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4coPoHcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54YrTGcUtYucTYWtUcTrBUshDhDh8AAo4g5HgGHPlrhmBYihkwkp77vle~1b~SEbHhrhhaFhrhrhhacBrWahrhrBi5lFAuNyQlhrFB5rBeWgaqj9B~V"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSHkvKGZD-w280-h280/hp-victus-15-fa0070t.webp",
        "productName": "HP Victus 15-fa0070TX Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹55,990",
        "rating": "4.75",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQC.Z2rg-jGexsQhrhAgTYBOr3Uh7tBc2YAUCFc54coPoHcYuUaTcAs3acY4c5oUtcWauc5oH4PtcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3AacWUDc5b4Pc5HHctyc54cgrPPGPUDcWrnhNcTrBUshDhDh8PX4oXiG5ialGrhmBYihkwkp77VV.SK-R._-_hrhhaFhrhrhhacBrWahrhrBi5XXNlyYg2hrFB51vlIB6A1d_Nb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVK3CMk0d-w280-h280/hp-15s-du3614tu-lapt.webp",
        "productName": "HP 15s-du3614TU Laptop (11th Gen Core i3/ 8GB/ 1TB 256GB SSD/ Win11 Home)",
        "price": "₹37,490",
        "rating": "4.2",
        "specScore": "61",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "256 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9x9Krq84~1uQznThrhAgTYBOr3Uh7tBc54FcYuUaTcAs3acYZc55UtcWauc5554WHcXcW6c5cU6ctiico4bcW6cFFic8Yuis8Fc55ctsnac54FciCZb5HUCcUtYucTYWtUcTrBUshDhDh8b5XaPPaArH6HXhmBYihkwkp77bZSV0zf14xHhrhhaFhrhrhhacBrWahrhrBi5XruN4NIihrFB5K-K5Ro-EGD2P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXRe5vKN-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HC-HN089WS Gaming Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹55,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G7vCXSfbx6ZAzWhrhAA3snrh7rFCFcUCgcWrnhNcYuUaTcAs3acY4c55UtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoP5lcW3rBthschncocZcOWch-hDZPZ4PbhrhhaFhrhrhhacBrWahrhrBi5snUBCCgFhrFB5Ugbg_Z4Tu-S1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuczPP204-w280-h280/dell-g15-5525-gaming.webp",
        "productName": "Dell G15-5525 Gaming Laptop (Ryzen 5 6600H/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹68,490",
        "rating": "4.2",
        "specScore": "57",
        "features": [
            "6th Gen AMD Ryzen 5  6600H",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI~Eyo~JDDR7DZ~hrhArnrysuhyihDRPR4SGxw0eh-hrhhaFhrhrhhacBrWahrhrBi5aTyXgl2ihrFB5Yn3PbZ_yyUQj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWsgvWznH-w280-h280/microsoft-surface-go.webp",
        "productName": "Microsoft Surface GO 2 8QF-00046 Laptop (11th Gen Core i5/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹54,990",
        "rating": "4",
        "specScore": "52",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Iris Xe Graphics",
            "12.4 inches, 1536 x 1024 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI9IRnCu4kC0IsQhrhArnrysuhyihDRPRHV-o5V0h-hrhhaFhrhrhhacBrWahrhrBi5CNiNNttshrFB5qK47HjWwAVRW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iB79FlVOf-w280-h280/acer-travelmate-tmp2.webp",
        "productName": "Acer TravelMate TMP214-53 Business Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹34,990",
        "rating": "4.35",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQYVJkimPqy5P4uhrhAgTYBOr3Uh7rAa3cU3r2aTnrUacYuUaTcAs3acY4c55UtcWauc55Z4WGc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacUnBo5Hc4ZcUtYucTYWtUcTrBUshDhDh8XHgrP66ogrloZhmBYihkwkp7EoKl-X~K-v07hrhhaFhrhrhhacBrWahrhrBi5uuDPAoNlhrFB5QsHQH0ZSZoNR"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1CuEUDbf-w280-h280/hp-pavilion-14-dv201.webp",
        "productName": "HP Pavilion 14-dv2015TU Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win 11)",
        "price": "₹76,990",
        "rating": "4.6",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PR1FaqU.qPpK-3hrhArnrysuhyihDRPR5pRx--oh-hrhhaFhrhrhhacBrWahrhrBi5i4Csy2QthrFB5Tj79_gkHyr1R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izDdf8D3L-w280-h280/hp-pavilion-14-dv205.webp",
        "productName": "HP Pavilion 14-dv2053TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win 11)",
        "price": "₹57,999",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xEjDP6vno70mxyhrhAgTYBOr3Uh7tBcBr2YTh3cYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5Hci2oP4ZUCcUtYucTYWtUcTrBUshDhDh8lPGlbAPgogXg5hmBYihkwkp7q7Z.Rz7wo0fJhrhhaFhrhrhhacBrWahrhrBi53Ia25C2lhrFB5o6Cbq83S-Un1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-is8ONy9MA-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED S3502ZA-L502WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹59,900",
        "rating": "4.75",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris XE Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ8m80k2aIWtmHUhrhAgTYBOr3Uh7rFCFcYuUaTcAs3acY4c5oUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFZ4PoyrcT4P58FcTrBUshDhDh8PaZ5bgoHAXZ5ahmBYihkwkp7.vG7.oEKfev7hrhhaFhrhrhhacBrWahrhrBi56XyDOG53hrFB5wV9m8xNuWeGt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy1VHUy48-w280-h280/asus-vivobook-s14-ol.webp",
        "productName": "Asus Vivobook S14 OLED S3402ZA-KM701WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹72,990",
        "rating": "4.6",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrE5eE0N0xlxt_xehrhAgTYBOr3Uh7rFCFc2Y2s6ssOcF5HcsTaicYuUaTca2sctcFa3YaFcAs3acYGc5oUtcWauc5oGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFZHPoyrcOnGPo8FcUtYucTYWtUcTrBUshDhDh8balAZlXo5iblihmBYihkwkp7w7o7wzfEfxHdhrhhaFhrhrhhacBrWahrhrBi5QOIaWWybhrFB5ijD89W~Cf.gP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i865vvNNE-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED K3502ZA-L701WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹72,990",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris XE Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrE5eE0N0xlxt_xehrhAgTYBOr3Uh7rFCFc2Y2s6ssOcF54csTaicYuUaTca2sctcFa3YaFcAs3acYGc5oUtcWauc5oGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacOZ4PoyrcTGP58FcUtYucTYWtUcTrBUshDhDh8Gri4XiGHr5gr4hmBYihkwkp7zofjGvR.fd.RhrhhaFhrhrhhacBrWahrhrBi5HHNBZOI3hrFB5jVG8EnkN4G8P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy67kSPjj-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 2023 E1504FA-NJ323WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹32,990",
        "rating": "4.25",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFq~Wpg78PyHo7rhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54coPoZcrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcuQZo58FcUtYucTYWtUcTrBUshDhDh8goirlAGPX4a56hmBYihkwkp7dvdEE7fvRlbjhrhhaFhrhrhhacBrWahrhrBi5nPsXX6WOhrFB5Ha37Wfn0Z78s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXwN4qHyM-w280-h280/lenovo-yoga-slim-7-p.webp",
        "productName": "Lenovo Yoga Slim 7 ProX 82TK00AFIN Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 4GB Graphics)",
        "price": "₹1,15,190",
        "rating": "4.55",
        "specScore": "75",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "14.5 inches, 3072 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBSm-W0l~YPWxNFfhrhArnrysuhyihDRPRvHwxzz_h-hrhhaFhrhrhhacBrWahrhrBi5PQANPAUthrFB5kA~AWtUd8GOB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icamBJvEM-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 OLED 2023 E1504FA-LK322WS Laptop (Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹39,990",
        "rating": "4.05",
        "specScore": "52",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFS6mwNZBvSVSBwhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54csTaicoPoZcrnic3IyaucZcNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcTOZo58FcUtYucTYWtUcTrBUshDhDh8ZiaXXgG5a44X6hmBYihkwkp7p7_xRoVfx7.dhrhhaFhrhrhhacBrWahrhrBi5bFylOX6rhrFB5TUYwCDf9TSa0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6KHeb5sN-w280-h280/asus-vivobook-go-15.webp",
        "productName": "Asus Vivobook Go 15 OLED 2023 E1504FA-LK521WS Laptop (Ryzen 5 7520U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹45,990",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzTlbzqQ0xQnJ8FhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcWsc54csTaicoPoZcrnic3Iyauc4cNCricAs3acG4oPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnaca54PHgrcTO4o58FcUtYucTYWtUcTrBUshDhDh8bia555AXr4G6lhmBYihkwkp7p7_xzGJJd7f7hrhhaFhrhrhhacBrWahrhrBi5iTY3a5BohrFB5qEHvC8~~qfwi"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZUJPXTx7-w280-h280/msi-katana-17-b13udx.webp",
        "productName": "MSI Katana 17 B13UDXK-255IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹74,990",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrO4U1uHmH_jWPJihrhAgTYBOr3Uh7nFYcOrUrurc5GcYuUaTcAs3acYGc5ZUtcWauc5ZboPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5HHctyc65ZCiDOco44YucWrnhNcTrBUshDhDh8PgAib6bP6g4XHhmBYihkwkp7p7e-SK_Jqwo7hrhhaFhrhrhhacBrWahrhrBi5bC6BF3iBhrFB58-F5Un~0EKWw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJeOh8tcP-w280-h280/infinix-inbook-y1-pl.webp",
        "productName": "Infinix INBook Y1 Plus Laptop (10th Gen Core i3/ 8GB/ 256GB SSD/ Win 11 Home)",
        "price": "₹26,990",
        "rating": "4.4",
        "specScore": "47",
        "features": [
            "10th Gen Intel Core i3 1005G1",
            "Dual Core, 4 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz.sO6TZQFWfnqIhrhAgTYBOr3Uh7YugYuYDcYu6ssOcI5cBTCFcoPoHcYuUaTcAs3acYZc5PUtcWauc5PP4W5cXcW6co4bcW6cFFic8Yuis8Fc55ctsnacDToXcUtYucTYWtUcTrBUshDhDh8oZHrX5arZoAgZhmBYihkwkp7ppZSf4qpdx.jhrhhaFhrhrhhacBrWahrhrBi5TryNIPD8hrFB5SAN~UeAqWzm6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZ3xwV9eq-w280-h280/hp-255-g8-laptop-amd.webp",
        "productName": "HP 255 G8 Laptop (AMD Athlon 3050U/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹22,710",
        "rating": "4.1",
        "specScore": "42",
        "features": [
            "3rd Gen AMD Athlon  3050U",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "‎AMD Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwkHp7jDZsj.32IhrhArnrysuhyihDRPR0~-4voSh-hrhhaFhrhrhhacBrWahrhrBi5WTgNBIC4hrFB5ApfyPaFIfvgA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igeKwE3uE-w280-h280/dell-inspiron-15-352.webp",
        "productName": "Dell Inspiron 15 3520 D560915WIN9S Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,780",
        "rating": "4.45",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFx7dOtuSY7tnDChrhAgTYBOr3Uh7iaTTcYuFBY3sucZ4oPcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacua8c54cTrBUsBcUtYucTYWtUh-hDh8oibaa5XPHGHXghmBYihkwkp7-G4S-7xK-b-dhrhhaFhrhrhhacBrWahrhrBi5rCZY3O5ihrFB5uCvlBfpaVfm4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6vI2Dy7k-w280-h280/primebook-4g-android.webp",
        "productName": "Primebook 4G Android Laptop (MediaTek MT8788/ 4GB/ 64GB eMMC/ Android 11)",
        "price": "₹14,990",
        "rating": "4.75",
        "specScore": "25",
        "features": [
            "MediaTek MTK8788",
            "Octa Core",
            "4 GB LPDDR4 RAM",
            "64 GB Hard Disk",
            "ARM Mali G72",
            "11.6 inches, 1366 x 768 pixels",
            "Android 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzz5m4gaW7Z~JAqhrhAgTYBOr3Uh7B3Yna6ssOcHWchY3sYic6rFaicnaiYrUaOcnUXGXXcHcW6cbHcW6cannAcFUs3rWacB3YnacsFcUtYucTYWtUcTrBUshDhDh8giZrZ54gAa5i4hmBYihkwkp7SodVf0.w0_jJhrhhaFhrhrhhacBrWahrhrBi5uPaa8rWrhrFB5N1tR8V45PUqa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwSj97kY4-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 3 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹69,990",
        "rating": "4.75",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25203%2520Laptop%2520(13th%2520Gen%2520Core%2520i5%252F%25208GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDlowbBvy-w280-h280/apple-macbook-air-m2.webp",
        "productName": "Apple MacBook Air M2 2022 Laptop (Apple M2/ 16GB/ 512GB SSD/ MacOS)",
        "price": "₹1,39,900",
        "rating": "4.45",
        "specScore": "44",
        "features": [
            "Apple M2 Apple M2 Chip",
            "Octa Core",
            "16 GB Unified Memory RAM",
            "512 GB SSD",
            "10-Core GPU",
            "13.6 inches, 2560 x 1664 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG0gPBOSY259B~GQhrhAgTYBOr3Uh7rBBTacoPoocnrA6ssOcrY3cnoc5bcW6c45ocW6cFFicnrAcsFcnsuhUaIcnTIoZtucrh-hDh8X4l64llZGb5A6hmBYihkwkpSoe.xvdx_~.EdhrhhaFhrhrhhacBrWahrhrBi5aN426FQlhrFB5CwWnU1Hb9oY8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixlZKisKj-w280-h280/dell-vostro-3420-lap.webp",
        "productName": "Dell Vostro 3420 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,990",
        "rating": "4",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58Ji3.R25t43l-u9lhrhAgTYBOr3Uh7iaTTcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic5bcannAcFUs3rWac8Yuis8Fc55ctsnac2sFU3scZHoPcUtYucTYWtUcTrBUshDhDh8ioXbZiH5ZZilahmBYihkwkp71X~0xqKVEVw7hrhhaFhrhrhhacBrWahrhrBi5a5inaiWnhrFB5Pgswa0_kwQs4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYn3CcnMP-w280-h280/hp-pavilion-14-dv201.webp",
        "productName": "HP Pavilion 14-dv2014TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹60,900",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6Pon6oZXtwYkVHohrhArnrysuhyihDRPR5plSfRzh-hrhhaFhrhrhhacBrWahrhrBi5ZDOi55FThrFB5F6BAEXn0qR-I"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqIz0PfCk-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-57 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹43,990",
        "rating": "4",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphic",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIwAFb.K9f-yG1JhrhArnrysuhyihDRPRSJ0zZo_h-hrhhaFhrhrhhacBrWahrhrBi5uZZD6AXihrFB5_bprnzPj3ZZj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuy2x9aE2-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 9 ‎‎QIX-00031 Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,92,990",
        "rating": "4.4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "13 inches, 2880 x 1920 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uIHS4iT0D~TdfP9xhrhAA3snrh7nYA3sFsgUcFC3grAacB3sclc8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtc5bW6c3rnc45oW6c3sncW3rBthsch-hDob44GbhrhhaFhrhrhhacBrWahrhrBi52GstABOrhrFB5Qys8Am47TEK9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqgrcwzCG-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 9 ‎QIL-00031 Laptop (12th Gen Core i7/ 16GB/ 256GB  SSD/ Win11)",
        "price": "₹1,62,990",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "256 GB SSD",
            "Intel Iris Xe Graphics",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9Xj0wEG9ZnS8dYuGhrhArnrysuhyihDRPRmfJ.R~4h-hrhhaFhrhrhhacBrWahrhrBi5CaZGDuA6hrFB5nRufW7-dyEU3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i68Sc9Fri-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2022 X1502ZA-EJ515WS Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹42,990",
        "rating": "4.2",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO901_Feaw6ZJO0tPhrhAgTYBOr3Uh7rFCFc2Y2s6ssOc54cYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacD54PoyrcaQ4548FcUtYucTYWtUcTrBUshDhDh84ooaigGigbX4XhmBYihkwkp7.K.e0RR.jVZ.hrhhaFhrhrhhacBrWahrhrBi5WuFAAZUihrFB53s2EHJztSwJp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i60YTYauf-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82RK007JIN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,990",
        "rating": "4.25",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "‎Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIGiB2vGV539qbBhrhArnrysuhyihDRPRGv_-JRHh-hrhhaFhrhrhhacBrWahrhrBi5a5B8N4bbhrFB58vD5AtxkvKUm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iylvexWIX-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 9 QEZ-00065 Laptop (12th Gen Core i5/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹96,335",
        "rating": "4.65",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB SSD",
            "Intel Iris Xe Graphics",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67~0jlAx9X.5gQrhrhArnrysuhyihDRPRmf.0KdHh-hrhhaFhrhrhhacBrWahrhrBi5DrHAurNDhrFB58bYbXk9nTT-_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iv8Jwpyar-w280-h280/lenovo-ideapad-flex.webp",
        "productName": "Lenovo IdeaPad Flex 5 82R90068IN Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹64,990",
        "rating": "4.5",
        "specScore": "69",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz8zeVY17AuPSanhrhAgTYBOr3Uh7Taus2scYiarBricgTaDc4crnic3IyaucGcsAUrcAs3ac4GPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HrTAGcoc5cTrBUshDhDh8Zo4HGGi5bHGlPhmBYihkwkp7SjlvS7V0Vx.KhrhhaFhrhrhhacBrWahrhrBi53QNZUZrXhrFB5rmjF~sPe~YsX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikr6NBJkU-w280-h280/chuwi-herobook-pro-l.webp",
        "productName": "Chuwi HeroBook Pro Laptop (Intel Celeron N4020/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹16,990",
        "rating": "4.7",
        "specScore": "42",
        "features": [
            "Intel ‎Celeron N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR3 RAM",
            "256 GB SSD",
            "Intel HD Graphics",
            "14.1 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Months Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FD8-EZDvfiC3O.shrhArnrysuhyihDRPKlv_SX_4h-hrhhaFhrhrhhacBrWahrhrBi5rZToa2tNhrFB5VYNubyHZTOCk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itvl6kLr2-w280-h280/agb-octev-ga-9009-ga.webp",
        "productName": "AGB Octev GA-9009 Gaming Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win 10 Pro/ 2GB Graph)",
        "price": "₹35,000",
        "rating": "4.1",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "2 GB NVIDIA Geforce MX450",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw0H.k0QzTd.lSahrhArnrysuhyihDRPlzoV1Z0Kh-hrhhaFhrhrhhacBrWahrhrBi5UaTXngYWhrFB5ZfPsFWT_9JOe"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0u2NYD8W-w280-h280/acer-one-14-z2-493-l.webp",
        "productName": "Acer One 14 Z2-493 Laptop (AMD Ryzen 3 3250U/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹23,990",
        "rating": "4.7",
        "specScore": "47",
        "features": [
            "3rd Gen AMD Ryzen 3  3250U",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ6ywYSTKkkEEI.hrhAgTYBOr3Uh7rAa3chFc5Hcrnic3IyaucZciCrTcAs3acZo4PCcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacyocHlZcUtYucTYWtUcTrBUshDhDh8iPoZPiZPiba4ZhmBYihkwkp7xSp-xSqKzKKHhrhhaFhrhrhhacBrWahrhrBi56ubriIUOhrFB54w3PF5tTu1OW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF9DZFPDC-w280-h280/acer-aspire-3-a315-5.webp",
        "productName": "Acer Aspire 3 A315-59 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹31,990",
        "rating": "4.2",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afryTrJ4bTloYvdqmhrhArnrysuhyihDRPRbx4JGJmh-hrhhaFhrhrhhacBrWahrhrBi5BTTAbrTGhrFB5HECEOU~osti8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEOSvWLBX-w280-h280/asus-vivobook-15-x51.webp",
        "productName": "Asus VivoBook 15 X515EA-EJ522WS Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹38,990",
        "rating": "4.15",
        "specScore": "56",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQOXUQra4mlePG3hrhAgTYBOr3Uh7rFCFc2Y2s6ssOc54coPoHcYuUaTcAs3acY4c55UtcWauc55Z4WGcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacD454arcaQ4oo8FcUtYucTYWtUcTrBUshDhDh86g66gGGHGrrP5hmBYihkwkp7xSd77JdK07efhrhhaFhrhrhhacBrWahrhrBi5WPGDoCPnhrFB5~upAnkf2BPEt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iu4j8LiSl-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 82SF008WIN Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹64,119",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqe4a5NY0_wmYO9hrhArnrysuhyihDRPR4bw10_4h-hrhhaFhrhrhhacBrWahrhrBi5H2sBP2Z6hrFB5VQvyk5BIKks2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDeaEnMek-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 82SF008YIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹58,491",
        "rating": "4.05",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xEeX.Z5CV5nyp.hrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4coPoHcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54YrTGcUtYucTYWtUcTrBUshDhDh8AAo4g5HgGHPlrhmBYihkwkp77vle~1b~SEbHhrhhaFhrhrhhacBrWahrhrBi5lFAuNyQlhrFB5rBeWgaqj9B~V"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWdm9Td9w-w280-h280/hp-pavilion-15s-fq51.webp",
        "productName": "HP Pavilion 15s-fq5112TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹50,690",
        "rating": "4.2",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58Ja5~n-atKmXFgG2hrhAgTYBOr3Uh7tBc54FcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgN455oUCcUtYucTYWtUcTrBUshDhDh8rgr5Gr5llirZ5hmBYihkwkp77bZSJdp_.VKxhrhhaFhrhrhhacBrWahrhrBi55O5UTtUHhrFB58OT5NaQ2meQm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVK3CMk0d-w280-h280/hp-15s-du3614tu-lapt.webp",
        "productName": "HP 15s-du3614TU Laptop (11th Gen Core i3/ 8GB/ 1TB 256GB SSD/ Win11 Home)",
        "price": "₹37,791",
        "rating": "4.2",
        "specScore": "61",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "256 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9x9VHyYU~DBRpyKhrhAgTYBOr3Uh7tBc54FcYuUaTcAs3acYZc55UtcWauc5554WHcXcW6c5cU6ctiico4bcW6cFFic8Yuis8Fc55ctsnac54FciCZb5HUCcUtYucTYWtUcTrBUshDhDh8b5XaPPaArH6HXhmBYihkwkp77bZSV0zf14xHhrhhaFhrhrhhacBrWahrhrBi5XruN4NIihrFB5K-K5Ro-EGD2P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXRe5vKN-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HC-HN089WS Gaming Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹55,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G7vCXSfbx6ZAzWhrhAA3snrh7rFCFcUCgcWrnhNcYuUaTcAs3acY4c55UtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcu2YiYrcWags3Aac3UDcZP4PcnFcsggYAacoP5lcW3rBthschncocZcOWch-hDZPZ4PbhrhhaFhrhrhhacBrWahrhrBi5snUBCCgFhrFB5Ugbg_Z4Tu-S1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOS7dujUa-w280-h280/asus-vivobook-16x-20.webp",
        "productName": "Asus Vivobook 16X 2022 M1603QA-MB511WS Laptop (Ryzen 5-5600H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹57,990",
        "rating": "4.75",
        "specScore": "62",
        "features": [
            "5th Gen AMD Ryzen 5 5600H",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Vega 7 Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afrQ8fuR5oJ5GdEmshrhArnrysuhyihDRPRmSHwSp0h-hrhhaFhrhrhhacBrWahrhrBi5OBU8UG56hrFB5fHfWVIkOiaTk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWsgvWznH-w280-h280/microsoft-surface-go.webp",
        "productName": "Microsoft Surface GO 2 8QF-00046 Laptop (11th Gen Core i5/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹54,990",
        "rating": "4",
        "specScore": "52",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Iris Xe Graphics",
            "12.4 inches, 1536 x 1024 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI9IRnCu4kC0IsQhrhArnrysuhyihDRPRHV-o5V0h-hrhhaFhrhrhhacBrWahrhrBi5CNiNNttshrFB5qK47HjWwAVRW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-is8ONy9MA-w280-h280/asus-vivobook-s15-ol.webp",
        "productName": "Asus Vivobook S15 OLED S3502ZA-L502WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹59,900",
        "rating": "4.75",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris XE Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQ8m80k2aIWtmHUhrhAgTYBOr3Uh7rFCFcYuUaTcAs3acY4c5oUtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFZ4PoyrcT4P58FcTrBUshDhDh8PaZ5bgoHAXZ5ahmBYihkwkp7.vG7.oEKfev7hrhhaFhrhrhhacBrWahrhrBi56XyDOG53hrFB5wV9m8xNuWeGt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1CuEUDbf-w280-h280/hp-pavilion-14-dv201.webp",
        "productName": "HP Pavilion 14-dv2015TU Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win 11)",
        "price": "₹78,990",
        "rating": "4.6",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af6PwVH-Yfbn4.YVUhrhArnrysuhyihDRPR5pRx--oh-hrhhaFhrhrhhacBrWahrhrBi5i4Csy2QthrFB5Tj79_gkHyr1R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izDdf8D3L-w280-h280/hp-pavilion-14-dv205.webp",
        "productName": "HP Pavilion 14-dv2053TU Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win 11)",
        "price": "₹58,990",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xEA2t8Qv8Efu4ghrhAgTYBOr3Uh7tBcBr2YTh3cYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5Hci2oP4ZUCcUtYucTYWtUcTrBUshDhDh8lPGlbAPgogXg5hmBYihkwkp7q7Z.Rz7wo0fJhrhhaFhrhrhhacBrWahrhrBi53Ia25C2lhrFB5o6Cbq83S-Un1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy1VHUy48-w280-h280/asus-vivobook-s14-ol.webp",
        "productName": "Asus Vivobook S14 OLED S3402ZA-KM701WS Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹69,990",
        "rating": "4.6",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i7 12700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzIQ201_A0PZowphrhAgTYBOr3Uh7rFCFc2Y2s6ssOcF5HcsTaicYuUaTca2sctcFa3YaFcAs3acYGc5oUtcWauc5oGPPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacFZHPoyrcOnGPo8FcUtYucTYWtUcTrBUshDhDh8balAZlXo5iblihmBYihkwkp7w7o7wzfEfxHdhrhhaFhrhrhhacBrWahrhrBi5QOIaWWybhrFB5ijD89W~Cf.gP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ictzSvUxr-w280-h280/hp-pavilion-15-eg200.webp",
        "productName": "HP Pavilion 15-eg2002TU Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹56,990",
        "rating": "4.2",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xᵉ Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz3E~lr-9bV-oHbhrhAgTYBOr3Uh7tBcBr2YTh3cYuUaTcAs3acY4c5oUtcWauc5oHPBc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacaWoPPoUCcUtYucTYWtUcTrBUshDhDh8A65rXlZGXoXaGhmBYihkwkp7E4.o7fz7VHJ.hrhhaFhrhrhhacBrWahrhrBi5sITCOaODhrFB5RuEjbAQf.2Qg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0ERCZRSl-w280-h280/asus-rog-zephyrus-m1.webp",
        "productName": "Asus ROG Zephyrus M16 GU603ZX-K8024WS Laptop (12th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 16GB Graph)",
        "price": "₹1,99,990",
        "rating": "4.05",
        "specScore": "83",
        "features": [
            "12th Gen Intel Core i9 12900H",
            "14 Cores (6P + 8E), 20 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 3080 Ti",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11  OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9XqFjO8835Of3jbDhrhArnrysuhyihDRPlJ-RoRKoh-hrhhaFhrhrhhacBrWahrhrBi55ZB5PlGuhrFB5~e6TRwCTGmrE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iD9Ibg2ks-w280-h280/asus-vivobook-k15-ol.webp",
        "productName": "Asus VivoBook K15 OLED KM513UA-L711WS Laptop (Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹61,500",
        "rating": "4.45",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 7  5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzCDoG0A82sF7UfhrhAgTYBOr3Uh7rFCFc2Y2s6ssOcO54csTaicrnic3IyaucGcsAUrcAs3ac3Gc4GPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacOn45ZCrcTG5o8FcUtYucTYWtUcTrBUshDhDh8X6HGglAgHoX5ZhmBYihkwkp7RbK.~-SSeqefhrhhaFhrhrhhacBrWahrhrBi5QXXBYFZFhrFB5DW1rkXt3QGY0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAaysIqYL-w280-h280/asus-vivobook-15-x51.webp",
        "productName": "Asus VivoBook 15 X515MA-BR011W Laptop (Celeron N4020/ 4GB/ 256GB SSD/ Win11 Home)",
        "price": "₹19,990",
        "rating": "4.3",
        "specScore": "33",
        "features": [
            "Intel Celeron  N4020",
            "Dual Core, 2 Threads",
            "4 GB  RAM",
            "256 GB SSD",
            "Intel UHD Graphics 600",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11  OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq5w0j2basTatRAhrhArnrysuhyihDRPle77RbXGh-hrhhaFhrhrhhacBrWahrhrBi52BWZYsWohrFB54TJpa_BKQNVK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMtPBCL4E-w280-h280/samsung-galaxy-book2.webp",
        "productName": "Samsung Galaxy Book2 Pro 360 13 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹83,490",
        "rating": "4.3",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "13.3 inches, 1080 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a.90sz6VY~FBGVrSehrhArnrysuhyihDRPl05xHHbwh-hrhhaFhrhrhhacBrWahrhrBi54QUUTa8UhrFB5V.RTbxzZwCqs"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ishl934oy-w280-h280/hp-14s-fq1092au-lapt.webp",
        "productName": "HP 14s-fq1092au Laptop (Ryzen 5 5500U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,500",
        "rating": "4.1",
        "specScore": "56",
        "features": [
            "5th Gen AMD Ryzen 5  5500U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9x~NoVosnd-k5n3hrhAgTYBOr3Uh7tBcrnic3Iyauc4ctaDrcAs3ac44PPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HFcgN5PlorCcUtYucTYWtUcTrBUshDhDh8HaboAZa6GHgG6hmBYihkwkp7j_XqfR..K_fbhrhhaFhrhrhhacBrWahrhrBi5aADylWQGhrFB5dlWJuleO3T56"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFun1cW3D-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2020 Z124J001KD Laptop (Apple M1/ 16GB/ 256GB SSD/ MacOS)",
        "price": "₹1,09,900",
        "rating": "4.15",
        "specScore": "43",
        "features": [
            "Apple M1",
            "Octa Core (4P + 4E)",
            "16 GB DDR4 RAM",
            "256 GB SSD",
            "Apple M1 Integrated Graphics",
            "13.3 inches, 2560 x 1600 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~xj-V~9eSmXHukohrhAgTYBOr3Uh7rBBTacoPoPcnrA6ssOcrY3cn5c5bcW6co4bcW6cFFicnrAcsFc6YWcFC3cnWubZtucrh-hDh8X5a6Al5rA4ZHXhmBYihkwkpSoe.xKz-.xKlHhrhhaFhrhrhhacBrWahrhrBi54X6OntPYhrFB5NQPS7DNl8Z9."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMIMPt8s6-w280-h280/dell-latitude-5420-l.webp",
        "productName": "Dell Latitude 5420 Laptop (11th Gen Core i7/ 16GB/ 512GB SSD/ Win10 Pro)",
        "price": "₹1,14,999",
        "rating": "4.2",
        "specScore": "56",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 10  OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~x2nZBoDPtqRsUkhrhAgTYBOr3Uh7iaTTcYuUaTcAs3acYGc55UtcWauc5bcW6c45ocW6cFFic8Yuis8Fc5PcB3scTrUYUCiac4HoPc6CFYuaFFcTrBUshDhDh8655iAGbXraA4rhmBYihkwkp7veHfbVz_z.0GhrhhaFhrhrhhacBrWahrhrBi5FZCYtbYFhrFB56~V1-y_vWe7_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixw8plkUF-w280-h280/hp-pavilion-15-ec200.webp",
        "productName": "HP Pavilion 15-ec2004AX Gaming Laptop (AMD Ryzen 5 5600H/ 8GB/ 512GB SSD/ Win10 Home/ 4GB Graph)",
        "price": "₹56,990",
        "rating": "4.1",
        "specScore": "62",
        "features": [
            "5th Gen AMD Ryzen 5  5600H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz3E~lr-9bV-oHbhrhAgTYBOr3Uh7tBcBr2YTh3crnic3Iyauc4ctaDrcAs3ac34c4bPPtcXcW6c45ocW6cFFic8Yuis8Fc5PcHcW3rBtYAFcu2YiYrcWags3AacWUDc5b4Pc5HHctyc54caAoPPHrDcWrnhNcTrBUshDhDh8b4gZXi4GHgH4ZhmBYihkwkp747._1Jp7zdJehrhhaFhrhrhhacBrWahrhrBi5P2BUTI6BhrFB5sD131VlP-_Z5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFTxBe0C0-w280-h280/realme-book-slim-lap.webp",
        "productName": "Realme Book Slim Laptop (11th Gen Core i3/ 8GB/ 256GB SSD/ Win10)",
        "price": "₹32,450",
        "rating": "4.7",
        "specScore": "48",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB LPDDR4x  RAM",
            "256 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1440 x 2160 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqlAs3Nz3t9OqiRhrhArnrysuhyihDRPlmb4-SGRh-hrhhaFhrhrhhacBrWahrhrBi5iBU4ryu4hrFB5__0v-WDWoJkl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9pWatI7J-w280-h280/asus-rog-flow-x13-gv.webp",
        "productName": "Asus ROG Flow X13 GV301QH-K5459TS Gaming Laptop (AMD Ryzen 9/ 32GB/ 1TB SSD/ Win10 Home/ 4GB Graph)",
        "price": "₹1,39,890",
        "rating": "4.2",
        "specScore": "79",
        "features": [
            "5th Gen AMD Ryzen 9  5980HS",
            "Octa Core, 16 Threads",
            "32 GB LPDDR4X RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce GTX 1650",
            "13.4 inches, 3840 x 2400 pixels, Touch Screen",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFRQbH86P5eVPq.sgRhrhAgTYBOr3Uh7rFCFc3sWcgTs8cD5ZcoPoHc3UDcZPXPcaWBCcrnic3IyauclcsAUrcAs3ac3lc4lXPtFcZocW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3AacWUDc5b4PcbPctycW2ZP5NtcO4H4lUFcoc5cWrnhNcTrBUshDhDh8XPiiaX5HbPAlbhmBYihkwkp7Z.xX_v.jS0zGhrhhaFhrhrhhacBrWahrhrBi5l3riaFsbhrFB53BVmeK~Y~HS5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-is2wSH0Ry-w280-h280/hp-15s-gr0011au-lapt.webp",
        "productName": "HP 15s-GR0011AU Laptop (AMD Ryzen 3/ 8GB/ 1TB HDD/ Win10 Home)",
        "price": "₹24,831",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "3rd Gen AMD Ryzen 3  3250U",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "1 TB Hard Disk",
            "AMD Radeon Vega 8",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9xR4QuPtqqkrieKhrhAgTYBOr3Uh7tBc54Fcrnic3IyaucZciCrTcAs3acZo4PCcXcW6c5cU6ctiic8Yuis8Fc5Pctsnac54FcW3PP55rCcUtYucTYWtUcTrBUshDhDh8rZaAArZi6rGl4hmBYihkwkpx.SxJqzzqxS0.hrhhaFhrhrhhacBrWahrhrBi5CFIYoUNPhrFB5KA_Dbjy1QoZ7"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijIIpnuMt-w280-h280/dell-latitude-3410-l.webp",
        "productName": "Dell Latitude 3410 Laptop (10th Gen Core i5/ 8GB/ 512GB SSD/ Ubuntu)",
        "price": "₹47,999",
        "rating": "4.65",
        "specScore": "52",
        "features": [
            "10th Gen Intel Core i5 10210U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel HD",
            "14 inches, 1366 x 768 pixels",
            "Ubuntu OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrznZ1Sb2igifViOhrhAgTYBOr3Uh7iaTTcTrUYUCiacYuUaTcAs3acY4c5PUtcWaucXcW6c45ocW6cFFicC6CuUCcZH5Pc6CFYuaFFcTrBUshDhDh8rb5XbPP4PXGXahmBYihkwkpxJ7GHqejE77GqhrhhaFhrhrhhacBrWahrhrBi5GnasUlB2hrFB5kNvGdaRgYNWC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igMLY9Q0A-w280-h280/hp-14-ck2018tu-lapto.webp",
        "productName": "HP 14-ck2018TU Laptop (10th Gen Core i5/ 8GB/ 512GB SSD/ Win10 Home)",
        "price": "₹39,990",
        "rating": "4.55",
        "specScore": "53",
        "features": [
            "10th Gen Intel Core i5 10210U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnO9x-9.NzZW.vmodThrhAgTYBOr3Uh7tBc5HcYuUaTcAs3acY4c5PUtcWauc5Po5PCcXcW6c45ocW6cFFic8Yuis8Fc5Pctsnac5HcAOoP5XUCcUtYucTYWtUcTrBUshDhDh8iHPo6iGr5blolhmBYihkwkpx0KoJ0.JRdV.jhrhhaFhrhrhhacBrWahrhrBi5ICBT66gbhrFB5pdpJaqwWavGm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip4KYw4KB-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2020 Laptop (10th Gen Core i3/ 8GB/ 256GB SSD/ MacOS)",
        "price": "₹72,999",
        "rating": "3.85",
        "specScore": "48",
        "features": [
            "10th Gen Intel Core i3",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel Iris Plus",
            "13.3 inches, 2560 x 1600 pixels",
            "Mac 10.15.3\t OS",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DApple%2520MacBook%2520Air%25202020%2520Laptop%2520(10th%2520Gen%2520Core%2520i3%252F%25208GB%252F%2520256GB%2520SSD%252F%2520MacOS)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iroQG5mxl-w280-h280/samsung-galaxy-chrom.webp",
        "productName": "Samsung Galaxy Chromebook Laptop (10th Gen Core i5/ 16GB/ 1TB SSD/ ChromeOS)",
        "price": "₹71,800",
        "rating": "4.2",
        "specScore": "55",
        "features": [
            "10th Gen Intel Core i5",
            "16 GB LPDDR3 RAM",
            "1 TB SSD",
            "Intel Integrated",
            "13.3 inches, 3840 x 2160 pixels, Touch Screen",
            "Chrome OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Chromebook%2520Laptop%2520(10th%2520Gen%2520Core%2520i5%252F%252016GB%252F%25201TB%2520SSD%252F%2520ChromeOS)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igjPi6GNE-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 Laptop (9th Gen Core i9/ 32GB/ 2TB SSD/ MacOS/ 4GB Graph)",
        "price": "₹2,01,498",
        "rating": "4.3",
        "specScore": "77",
        "features": [
            "9th Gen Intel Core i9",
            "Octa Core",
            "32 GB DDR4 RAM",
            "2 TB SSD",
            "4 GB Radeon Pro 5500M",
            "16 inches, 3072 x 1920 pixels",
            "Mac Catalina OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DApple%2520MacBook%2520Pro%252016%2520Laptop%2520(9th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25202TB%2520SSD%252F%2520MacOS%252F%25204GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXaqFsEMl-w280-h280/dell-inspiron-5370-l.webp",
        "productName": "Dell Inspiron 5370 Laptop (8th Gen Core i7/ 8GB/ 256GB SSD/ Win10/ 4GB Graph)",
        "price": "₹87,990",
        "rating": "4.7",
        "specScore": "61",
        "features": [
            "8th Gen Intel Core i7 8550U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "4 GB Geforce MX130",
            "13.3 inches, 1920 x 1080 pixels",
            "Windows 10 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY_d3a7AEssB0KVhrhAgTYBOr3Uh7iaTTcYuFBY3suc4ZGPcYuUaTcAs3acYGcXUtcWaucX44PCcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcrnic3riasuc4ZPcWrnhNcTrBUshDhDh8655gHoAa4ZoA4hmBYihkwkpxVfSxSl1xfvl7hrhhaFhrhrhhacBrWahrhrBi5gTIo88XFhrFB5pE6zOjyXRt3O"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipn1WiDHX-w280-h280/acer-aspire-5-nx-khf.webp",
        "productName": "Acer Aspire 5 NX.KHFSI.007 Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,990",
        "rating": "4.5",
        "specScore": "51",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZU.0isjzgiiC1nhrhAA3snrh7rAa3crFBY3ac4cYuUaTcAs3acY4c5ZUtcWaucUtYucTYWtUcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5cFUaaTcW3rIc5cG4cOWch-hDZPbl5lhrhhaFhrhrhhacBrWahrhrBi5XTuGGuIXhrFB553K_r3iCTjG4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9vtVNUxF-w280-h280/acer-aspire-3-spin-1.webp",
        "productName": "Acer Aspire 3 Spin 14 NX.KENSI.004 Laptop (Intel Core i3 N305/ 8GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹39,990",
        "rating": "4.2",
        "specScore": "47",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZODYnTeV8NHaOIhrhAA3snrh7rAa3crFBY3acZcFBYucYuUaTcAs3acYZcUsCAtFA3aaucocYuc5cTrBUsBcXW6c45oW6cFFic8Yuis8Fc55cB3sc5HcYuAtc8CDWrcYBFciYFBTrIcnFcsggYAacoPo5cBC3acFYThCc5c4HcOWch-hDZPbloPhrhhaFhrhrhhacBrWahrhrBi5PtGBb2Z5hrFB5rIaOBmSa0lZZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieUEPbGU3-w280-h280/hp-pavilion-16-ai-16.webp",
        "productName": "HP Pavilion 16 AI 16-ag0019AU Laptop (AMD Ryzen 5 8540U/ 16GB / 512GB SSD/ Win11)",
        "price": "₹68,630",
        "rating": "4.2",
        "specScore": "62",
        "features": [
            "8th Gen AMD Ryzen 5 8540U",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rws-yS331NagjTmhrhArnrysuhyihDRPKoblo.xph-hrhhaFhrhrhhacBrWahrhrBi5GrOQUnBihrFB5iQ4-s_IHr0u-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7NZQkiwN-w280-h280/msi-stealth-18-merce.webp",
        "productName": "MSI Stealth 18 Mercedes AMG Motorsport Gaming Laptop (Intel Core Ultra 9/ 32GB/ 1TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹3,19,990",
        "rating": "4",
        "specScore": "92",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMSI%2520Stealth%252018%2520Mercedes%2520AMG%2520Motorsport%2520Gaming%2520Laptop%2520(Intel%2520Core%2520Ultra%25209%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%252012GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUZiDSh2V-w280-h280/lenovo-thinkpad-p16s.webp",
        "productName": "Lenovo ThinkPad P16s 21K9S00C00 Laptop (AMD Ryzen 7 Pro 7840U/ 32GB/ 1TB SSD/ Win11 Pro)",
        "price": "₹1,06,485",
        "rating": "4.65",
        "specScore": "71",
        "features": [
            "7th Gen AMD Ryzen 7 7840U",
            "Octa Core, 16 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "AMD Radeon 700M Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzP2OssoT_8V9Q.hrhArnrysuhyihDRPKbGSKbZzh-hrhhaFhrhrhhacBrWahrhrBi5s3BHCYWQhrFB5U3U~S17ReRaO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ialrO1UlA-w280-h280/hp-probook-440-g9-9s.webp",
        "productName": "HP ProBook 440 G9 9S706AT Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹69,899",
        "rating": "4.7",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rws3JHJdykw0rt5hrhArnrysuhyihDRPKXGlfRbmh-hrhhaFhrhrhhacBrWahrhrBi5lr3QgYr4hrFB5k8_Ued.baS~E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8SiCU5T0-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15  B12MO-1007IN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹42,990",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw.8ed8A1z-XOpmhrhArnrysuhyihDRPKlm05vvSh-hrhhaFhrhrhhacBrWahrhrBi52isuHtuohrFB52~TKJg80~~4G"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBio9uxUA-w280-h280/msi-modern-15-b12uc.webp",
        "productName": "MSI Modern 15 B12UC-2086IN Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home/4GB Graphics)",
        "price": "₹62,990",
        "rating": "4.55",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwTYC4jGvAkIx.ThrhArnrysuhyihDRPKo-5GSd-h-hrhhaFhrhrhhacBrWahrhrBi54sYnHNs5hrFB5SGEt6mw~-kHA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFSAuNBzu-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15 B12MO-1006IN Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹54,990",
        "rating": "4.1",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwWQ3Co5z487yy4hrhArnrysuhyihDRPKXJVoHfbh-hrhhaFhrhrhhacBrWahrhrBi58DQlN6y6hrFB5EKzs7ujeCDwd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHUCaFx5X-w280-h280/thomson-neo-15-in-n1.webp",
        "productName": "Thomson Neo 15 IN-N15I312-8GR512 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/Win11 Home)",
        "price": "₹27,990",
        "rating": "4.4",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtIoJfAGkpaX7QDhrhAgTYBOr3Uh7UtsnFsucuascAs3acFa3YaFcYuUaTcYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacYucu54YcUtYucTYWtUcTrBUshDhDh8lArA54oba5XHXhmBYihkwkp7__xo~_f7.ESbhrhhaFhrhrhhacBrWahrhrBi536l6snGthrFB5FjJO5qkX-8wb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ib5cQU8XL-w280-h280/huawei-matebook-gt-1.webp",
        "productName": "Huawei MateBook GT 14 Laptop (Intel Core Ultra 9 185H/ 32GB/ 2TB SSD/ Win11)",
        "price": "₹1,27,990",
        "rating": "4.35",
        "specScore": "69",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB  RAM",
            "2 TB SSD",
            "Intel Arc Graphics",
            "14.2 inches, 1920 x 2880 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHuawei%2520MateBook%2520GT%252014%2520Laptop%2520(Intel%2520Core%2520Ultra%25209%2520185H%252F%252032GB%252F%25202TB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTB7ztoGk-w280-h280/hp-victus-15-fa1321t.webp",
        "productName": "HP Victus 15-fa1321TX Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX3050 Graph)",
        "price": "₹93,990",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFsqG9Z6-q-j9~phrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acYGc5ZUtcWauc5ZboPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc54cgr5Zo5UDcWrnhNcTrBUshDhDh8Gr4b5GiHiGAaohmBYihkwkpSxvHxf17JzGJ4hrhhaFhrhrhhacBrWahrhrBi5NAN8lTFPhrFB5KrtFrHe3oQ_o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipU4LQZyf-w280-h280/lenovo-thinkpad-e16.webp",
        "productName": "Lenovo Thinkpad E16 G1 21JNS0QD00 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹49,485",
        "rating": "4.2",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwA8w8Bjj1VH_qohrhArnrysuhyihDRPKHfmGxplh-hrhhaFhrhrhhacBrWahrhrBi5Ob2iHXOQhrFB5Nyas_6827XdE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifiCx5vFR-w280-h280/dell-latitude-7455-a.webp",
        "productName": "Dell Latitude 7455 AI Laptop (Snapdragon X Elite/ 16GB/ 512GB SSD/ Windows 11 Home)",
        "price": "₹1,59,990",
        "rating": "4.6",
        "specScore": "53",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-80-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "14 inches, 2560 x 1600 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DDell%2520Latitude%25207455%2520AI%2520Laptop%2520(Snapdragon%2520X%2520Elite%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Windows%252011%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIOANDRNb-w280-h280/dell-inspiron-5640-l.webp",
        "productName": "Dell Inspiron 5640 Laptop (Intel Core 7 150U Processor/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹92,590",
        "rating": "4.35",
        "specScore": "56",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKZx2WlGKOu6a8GhrhArnrysuhyihDRPKZm7eRoJh-hrhhaFhrhrhhacBrWahrhrBi5iQTUgNOChrFB50qxZf2m0Ha53"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i10OpbNbx-w280-h280/msi-modern-14-c12mo.webp",
        "productName": "MSI Modern 14 C12MO-1211IN Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹51,990",
        "rating": "4.15",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwgdrks_aTsvOe_hrhArnrysuhyihDRPR0oxxG57h-hrhhaFhrhrhhacBrWahrhrBi5niW4TCoBhrFB5H81IyCgR7aAv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0sq0FF4Z-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS13M00 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹67,990",
        "rating": "4.5",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwuydx3xuEA5PGmhrhArnrysuhyihDRPKbGox_Xoh-hrhhaFhrhrhhacBrWahrhrBi56Hg3sCXQhrFB5bonmiG5UCFBB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAZ0PuT5u-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS1CQ00 Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹75,490",
        "rating": "4.2",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFu6E8oZ1JVwXZhrhArnrysuhyihDRPKH~fdwJeh-hrhhaFhrhrhhacBrWahrhrBi5WaABG6AbhrFB5TXjmf~9o6Fet"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJLmfTSg3-w280-h280/hp-victus-special-ed.webp",
        "productName": "HP Victus Special Edition 15-fa1379TX Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ RTX 3050A)",
        "price": "₹69,990",
        "rating": "4.05",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050A",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYp06AJnPw2PnRBhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Prc54cgr5ZGlUDcWrnhNcTrBUshDhDh8lAZGXr4Z4lPbghmBYihkwkpSoKf.EjRSS~.jhrhhaFhrhrhhacBrWahrhrBi5Tg3D6QFGhrFB5WE9OsVWaZ-2S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyR68H5fw-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios 16 NH.QNXSI.004 Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB RTX4070)",
        "price": "₹1,89,990",
        "rating": "4.5",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG6NKu09Rzts8V1yhrhAgTYBOr3Uh7rAa3cBhBrUs3ctaTYsFc5bcYuUaTcAs3acYGc5HUtcWauc5HGPPtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPGPcBt5bcGocWrnhNcTrBUshDhDh8ZHgbXAolbAab4hmBYihkwkpSxSe.0xfedx7fhrhhaFhrhrhhacBrWahrhrBi58aTyHAyBhrFB565rk-GqxB-JE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWO2u6O10-w280-h280/asus-chromebook-cx14.webp",
        "productName": "Asus Chromebook CX1400CKA-NK0453 Laptop (Celeron N4500/ 4GB/ 64GB eMMC/ Chrome OS)",
        "price": "₹18,990",
        "rating": "4.05",
        "specScore": "33",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "4 GB LPDDR4X RAM",
            "64 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwVymNfVzU2oyr-hrhArnrysuhyihDRPKGJGwX5Kh-hrhhaFhrhrhhacBrWahrhrBi52QDuOUrahrFB5-Fzp-zZgOPox"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRPypy31Q-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82XN006MIN Laptop (AMD Ryzen 3 7320U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹31,990",
        "rating": "4.55",
        "specScore": "53",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY5KRknCSn8kJ9.hrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcrnic3IyaucNCricAs3acGZoPCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HrnuXcUtYucTYWtUcTrBUshDhDh8AglHii4oPlbGbhmBYihkwkpSxf.Z7f7x7~..hrhhaFhrhrhhacBrWahrhrBi564ZyN8AOhrFB5BuJqvQqObJaT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipS3kFdFo-w280-h280/lenovo-yoga-book-9-8.webp",
        "productName": "Lenovo Yoga Book 9 83FF0034IN Laptop (Intel Evo Core Ultra 7 155U/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,38,990",
        "rating": "4.3",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 155U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Integrated Graphics",
            "13.3 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJuP7vQPiNn9praRhrhArnrysuhyihDRPKH447zozh-hrhhaFhrhrhhacBrWahrhrBi588l8UOgXhrFB5eSIlX4qB1HYb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iux12d7Lh-w280-h280/hp-victus-special-ed.webp",
        "productName": "HP Victus Special Edition 15-fa1382TX Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ RTX 3050A)",
        "price": "₹78,990",
        "rating": "4.35",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050A",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEHRZJSe3u0po9fhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acYGc5oUtcWauc5ob4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Prc54cgr5ZXoUDcWrnhNcTrBUshDhDh8GlgXG5oaZAiXlhmBYihkwkpSoKf.7qE-Hz4ehrhhaFhrhrhhacBrWahrhrBi5y6nYugrUhrFB5mX0Zz0~gB5o_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuRYHX1cg-w280-h280/hp-pavilion-15-eg313.webp",
        "productName": "HP Pavilion 15-eg3130TU Laptop (13th Gen Core i3/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹52,485",
        "rating": "4.45",
        "specScore": "48",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB  RAM",
            "256 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgaTD7GuZ.Qk.GhrhArnrysuhyihDRPKXfv~m71h-hrhhaFhrhrhhacBrWahrhrBi5y4nTt24YhrFB5jtdQvRo56ikB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNI96kt2f-w280-h280/lenovo-ideapad-1-15a.webp",
        "productName": "Lenovo IdeaPad 1 15ALC7 82R400EFIN Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹44,990",
        "rating": "4.05",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYXeWOAXARAXJ~BhrhAgTYBOr3Uh7Taus2scYiarBric5crnic3IyaucGcsAUrcAs3ac4GPPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54rTAGcUtYucTYWtUcTrBUshDhDh8lgiiaPXHr5aAbhmBYihkwkpSf7X.K01zEffRhrhhaFhrhrhhacBrWahrhrBi5YNaGZnb4hrFB5O5TnKAxf42b1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuEZEgeET-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS13L00 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹48,999",
        "rating": "4.2",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwAgXJnGAydmRu9hrhArnrysuhyihDRPKbbfVvz.h-hrhhaFhrhrhhacBrWahrhrBi5btDo45aFhrFB5.B_TUnzVCZxW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTUOwcqvt-w280-h280/acer-travelmate-tmp2.webp",
        "productName": "Acer TravelMate TMP215-53 Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹60,780",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwOOqXxVYKJRPx5hrhArnrysuhyihDRPKlKwHJxHh-hrhhaFhrhrhhacBrWahrhrBi552XbnF3DhrFB5NZV3bV1SpX6u"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKQG0uB0w-w280-h280/thomson-neo-series-i.webp",
        "productName": "Thomson Neo Series IN-PX14C  Laptop (Intel Celeron N4020/ 4 GB/128 GB SSD/Win11 Home)",
        "price": "₹16,490",
        "rating": "4.15",
        "specScore": "33",
        "features": [
            "Intel Celeron N4020",
            "Dual Core, 2 Threads",
            "4 GB LPDDR4 RAM",
            "128 GB SSD",
            "Intel Integrated UHD",
            "14.1 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFt3Jk8KKFC0KYoThrhAgTYBOr3Uh7UtsnFsucYuUaTcAaTa3suciCrTcAs3acuHPoPcHcW6c5oXcW6cFFic8Yuis8Fc55ctsnacYucBD5HAcUtYucTYWtUcTrBUshDhDh8gb55lrHa4r6rahmBYihkwkpSfl7SVvS11j77hrhhaFhrhrhhacBrWahrhrBi5gAIl454BhrFB5sTZmACYrWs~Q"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAcsgutaF-w280-h280/lenovo-thinkpad-p14s.webp",
        "productName": "Lenovo ThinkPad P14s 21K5S00F00 Laptop (AMD Ryzen 7 Pro 7840U/ 32GB/ 1TB SSD/ Win11 Pro)",
        "price": "₹1,13,999",
        "rating": "4.65",
        "specScore": "73",
        "features": [
            "7th Gen AMD Ryzen 7 7840U",
            "Octa Core, 16 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJEPlSaHTDCqtO0xhrhArnrysuhyihDRPKbGwp5xXh-hrhhaFhrhrhhacBrWahrhrBi54CPtoBZnhrFB5UnUst5STTefa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iV1bVCdfI-w280-h280/dell-vostro-5630-bus.webp",
        "productName": "Dell Vostro 5630 Business Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹84,490",
        "rating": "4.2",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Integrated",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY0NnwysDFx1zSthrhAgTYBOr3Uh7iaTTc2sFU3sc4bZPcYuUaTcAs3acYGc5ZUtcWauc5ZbPBc5bcW6c45ocW6cFFic8Yuis8Fc55cB3sc5bc6CFYuaFFcTrBUshDhDh8GGiabHlaGZZlrhmBYihkwkpSodXf-ed~p-J1hrhhaFhrhrhhacBrWahrhrBi5NybyI3bahrFB5P6g23Q9TIKPz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9k1K8Bml-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS1FT00 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹86,990",
        "rating": "4.7",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwy-QGV2f3gqk_7hrhArnrysuhyihDRPKXHZ7lRdh-hrhhaFhrhrhhacBrWahrhrBi5HiOoo6CQhrFB5w_nIKo~zRe1Z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iP16UGCob-w280-h280/hp-15s-fc0156au-lapt.webp",
        "productName": "HP 15s-fc0156AU Laptop (AMD Ryzen 5 7520U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹47,999",
        "rating": "4",
        "specScore": "59",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwAKoto9pKVQu.ThrhArnrysuhyihDRPwfo1m~Xdh-hrhhaFhrhrhhacBrWahrhrBi5OXIOaPNahrFB53O2SZxCJqkqj"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irTiMsp2w-w280-h280/hp-15-fc0155au-lapto.webp",
        "productName": "HP 15-fc0155AU Laptop (AMD Ryzen 5 7520U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹45,799",
        "rating": "4.25",
        "specScore": "56",
        "features": [
            "7th Gen AMD Ryzen 5 7520U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw6q_ZX02AADJophrhArnrysuhyihDRPwfov57Z7h-hrhhaFhrhrhhacBrWahrhrBi5sUYH23IAhrFB5T5.TlOWtzZkN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2bW2mZIS-w280-h280/air-falcon-series-la.webp",
        "productName": "Air Falcon Series laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹28,990",
        "rating": "4.2",
        "specScore": "45",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw~F.tjHyypjbQlhrhArnrysuhyihDRPKGpwxVl_h-hrhhaFhrhrhhacBrWahrhrBi52oN8PYi5hrFB5OQJ7QaNnkJxt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i40cCyj9f-w280-h280/air-falcon-series-14.webp",
        "productName": "Air Falcon Series 14ADL5 laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹36,990",
        "rating": "4.45",
        "specScore": "47",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw036F9jI0s3p-BhrhArnrysuhyihDRPKGpw5v_Jh-hrhhaFhrhrhhacBrWahrhrBi5a42WPuUIhrFB5YJBur-~rC64y"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5wMw2O7X-w280-h280/thomson-neo-15-in-n1.webp",
        "productName": "Thomson Neo 15 IN-N15I312 Laptop (12th Gen Core i3/ 8GB/ 256GB SSD/Win11 Home)",
        "price": "₹27,490",
        "rating": "4.2",
        "specScore": "51",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtD3YAfugT4OKlyhrhAgTYBOr3Uh7UtsnFsucuascAs3acFa3YaFcYuUaTcYZc5oUtcWauc5o54CcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacYucu54YcUtYucTYWtUcTrBUshDhDh8GPGZ5o5XogrlXhmBYihkwkp7__xofVvSKzzEhrhhaFhrhrhhacBrWahrhrBi5gnQulCy8hrFB5dnQvPCBDr5pr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivLK9svnC-w280-h280/thomson-neo-15-in-n1.webp",
        "productName": "Thomson Neo 15  IN-N15I712 Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/Win11 Home)",
        "price": "₹43,990",
        "rating": "4.5",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYXPrCF-m1.JT2-hrhAgTYBOr3Uh7UtsnFsucuascAs3acFa3YaFcYuUaTcYGc5oUtcWauc5o44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacYucu54YcUtYucTYWtUcTrBUshDhDh8g5aZlGaHAi5HlhmBYihkwkp7__xovJ1l~p-ehrhhaFhrhrhhacBrWahrhrBi5XIbPWC36hrFB5BUs0-ng6EqP_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYyMmOIZh-w280-h280/thomson-neo-15-in-n1.webp",
        "productName": "Thomson Neo 15 IN-N15I512-8GR512 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/Win11 Home)",
        "price": "₹36,990",
        "rating": "4.45",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYZza.Eoiglv7NlhrhAgTYBOr3Uh7UtsnFsucuascAs3acFa3YaFcYuUaTcY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacYucu54YcUtYucTYWtUcTrBUshDhDh86AZXZAr5G6GGAhmBYihkwkp7__xoVR1..1JShrhhaFhrhrhhacBrWahrhrBi5aGOBNuP4hrFB57Vptw7PWamIv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYyMmOIZh-w280-h280/thomson-neo-15-in-n1.webp",
        "productName": "Thomson Neo 15 IN-N15I Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/Win11 Home)",
        "price": "₹37,990",
        "rating": "4.7",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYZ2O1K3CvwZ5mghrhAgTYBOr3Uh7UtsnFsucuascAs3acFa3YaFcYuUaTcY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacYucu54YcUtYucTYWtUcTrBUshDhDh84aaGA65gAaP6ghmBYihkwkp7__xoS7GwwfRvhrhhaFhrhrhhacBrWahrhrBi58YtAY68yhrFB5G5rp_6NuOgEB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iW78s4fM6-w280-h280/hp-chromebook-14a-nf.webp",
        "productName": "HP Chromebook 14a-nf0017tu Laptop (Intel Core i3-N305/ 8GB/ 256GB UFS/ Chrome OS)",
        "price": "₹47,490",
        "rating": "4.45",
        "specScore": "41",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1080 x 1920 pixels, Touch Screen",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqSuRGKd83FrgrihrhArnrysuhyihDRPKboR.fmbh-hrhhaFhrhrhhacBrWahrhrBi5Q5Ta88l4hrFB5i.aT5DRgpYrG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivIPZhOPM-w280-h280/hp-omnibook-ultra-ne.webp",
        "productName": "HP OmniBook Ultra Next Gen AI PC Laptop (AMD Ryzen AI 300 Series Processors/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,59,990",
        "rating": "4.05",
        "specScore": "56",
        "features": [
            "AMD Ryzen AI 300",
            "32 GB  RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 2240 x 1400 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520OmniBook%2520Ultra%2520Next%2520Gen%2520AI%2520PC%2520Laptop%2520(AMD%2520Ryzen%2520AI%2520300%2520Series%2520Processors%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7rV0Pbcb-w280-h280/dell-xps-9345-ai-lap.webp",
        "productName": "Dell XPS 9345 AI Laptop (Snapdragon X Elite X1E-80-100/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,70,690",
        "rating": "4.7",
        "specScore": "74",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-80-100",
            "12 Cores",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "13.4 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ6b.xt9IenmKTRBhrhArnrysuhyihDRPKXReGe7oh-hrhhaFhrhrhhacBrWahrhrBi5BG4bgo8OhrFB5roU33Aysb.mA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1BAjxj0u-w280-h280/dell-xps-13-9345-ai.webp",
        "productName": "Dell XPS 13 9345 AI Laptops (Snapdragon X Elite X1E-80-100/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,41,490",
        "rating": "4.25",
        "specScore": "65",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-80-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.4 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ_zs.822lbBKAAYhrhArnrysuhyihDRPKXR1-e_wh-hrhhaFhrhrhhacBrWahrhrBi5aBOUPG4DhrFB55dXpq5s3ovWB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibMuoMgQo-w280-h280/dell-xps-9345-ai-lap.webp",
        "productName": "Dell XPS 9345 AI Laptops (Snapdragon X Elite/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,51,190",
        "rating": "4.2",
        "specScore": "69",
        "features": [
            "Qualcomm Snapdragon X Elite X1E-80-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.4 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJftow~wi0vjtayphrhArnrysuhyihDRPKXRv7H41h-hrhhaFhrhrhhacBrWahrhrBi5aolnZtQghrFB5l4JRNkd2foxP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTmyPtCwN-w280-h280/hp-chromebook-x360-1.webp",
        "productName": "HP Chromebook x360 14b-cd0012TU Laptop (Intel Processor N200/ 8GB/ 128GB UFS/ Chrome OS)",
        "price": "₹40,785",
        "rating": "4.05",
        "specScore": "37",
        "features": [
            "Intel N200 N200",
            "Quad Core, 4 Threads",
            "8 GB LPDDR5 RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF-m9qX-6Ab7suChrhAgTYBOr3Uh7tBcYuUaTcAs3acucuoPPcXcW6c5oXcW6cAt3snacsFc5H6cAiPP5oUCcAt3sna6ssOcTrBUshDhDh8oga6abiabA5HghmBYihkwkpSo04fz~zS0.7dhrhhaFhrhrhhacBrWahrhrBi5CtCF3nD4hrFB5BRBl-fPjK7kx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWmLxaV9h-w280-h280/acer-aspire-3-15-a32.webp",
        "productName": "Acer Aspire 3 15 A325-45 Laptop (Intel Core Celeron N4500/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹20,990",
        "rating": "4.2",
        "specScore": "33",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "256 GB SSD",
            "Intel UHD",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz_bR6VbGq~CSRFhrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacrZo4cH4cUtYucTYWtUcTrBUshDhDh84GGral6liP6a4hmBYihkwkpSoz1eSw7fSSSXhrhhaFhrhrhhacBrWahrhrBi5XCXsiFOQhrFB55TX67pjxtQNo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqlzdOiia-w280-h280/acer-aspire-3d-15-sp.webp",
        "productName": "Acer Aspire 3D 15 SpatialLabs Edition  A3D15-71GM 3D Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB RTX 4050)",
        "price": "₹1,74,990",
        "rating": "4.4",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 3840 x 2160 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGrXRn-j-jR1XJ5_hrhAgTYBOr3Uh7rAa3crFBY3acZic54cFBrUYrTTr6FcYuUaTcAs3acYGc5ZUtcWauc5ZboPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHP4PcrZi54cG5WncWrnhNcTrBUshDhDh8bXX44XrlZGlGahmBYihkwkpSoKZljZK._VwKhrhhaFhrhrhhacBrWahrhrBi5rIl4XYCnhrFB5X1b0C59~Xzrv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikTCMgSLR-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 15 ‎ZHH-00048 (Snapdragon X Elite/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,59,990",
        "rating": "4.05",
        "specScore": "48",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB ‎LPDDR5x RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "15 inches, 2496 x 1664 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.u7qdn7U-05g7PK9rhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cYuAtcTAiciYFBTrIchnc5cbbcOWch-hDZPX4o5hrhhaFhrhrhhacBrWahrhrBi5G6gAHab5hrFB5k8_3JfE5GCpC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJPiJkDaT-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 11 ‎ZIB-00031 Laptop (Snapdragon X Elite/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,80,990",
        "rating": "4.45",
        "specScore": "53",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uIoNQ9b1k0jooB9_hrhAA3snrh7nYA3sFsgUcFC3grAacB3sc55UtcaiYUh3c8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtc5bW6c3rnc5U6c3snchnch-hDZPX4oGhrhhaFhrhrhhacBrWahrhrBi5P2X8tUIXhrFB5ProgPFBpFPfF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJPiJkDaT-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 11 2024 ‎ZID-00014 Laptop (Snapdragon X Elite/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,32,990",
        "rating": "4.6",
        "specScore": "59",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgI_dSzdK4-qpFHAhrhAA3snrh7nYA3sFsgUcFC3grAacB3sc55UtcaiYUh3c8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtcZoW6c3rnc5U6c3sncBTrUYuCnch-hDZPX4oXhrhhaFhrhrhhacBrWahrhrBi5s8T6X3nQhrFB5Oq46-G19xZox"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4qDKdISf-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 11 2024 ‎ZHY-00032 Laptop (Snapdragon X Plus/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,31,990",
        "rating": "4.5",
        "specScore": "50",
        "features": [
            "Qualcomm Snapdragon X Plus",
            "10 Cores",
            "16 GB LPDDR5x RAM",
            "256 GB SSD",
            "Qualcomm Adreno GPU",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgYdD-D0EfzIPwGChrhAA3snrh7nYA3sFsgUcFC3grAacB3sc55UtcaiYUh3c8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtc5bW6c3rnc45oW6c3sncBTrUYuCnch-hDZPX4oohrhhaFhrhrhhacBrWahrhrBi5AlyCsgHQhrFB5HveK_KOaZp90"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isksWFMpJ-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 13.8 ‎‎ZGQ-00023 (Snapdragon X Elite/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,02,990",
        "rating": "4.25",
        "specScore": "52",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "32 GB ‎LPDDR5x RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "13.8 inches, 2304 x 1536 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uIlK1xgKdeZx~mFvhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBcZoW6c5U6cFFic8Yuis8Fc55ctsnac5ZcXcYuAtcTAiciYFBTrIchnc5cZHcOWch-hDZPX45bhrhhaFhrhrhhacBrWahrhrBi5Hn8bA6yuhrFB5VwWEVU7zJgO3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isksWFMpJ-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 ‎ZXX-00059 (Snapdragon X Elite/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,70,990",
        "rating": "4.35",
        "specScore": "46",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB  RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "13.8 inches, 2304 x 1536 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uI5AlkGyoENHHQUyhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnac5ZcXcYuAtcTAiciYFBTrIchnc5cZHcOWch-hDZPX45GhrhhaFhrhrhhacBrWahrhrBi52rYA4FDohrFB5RUNE1STIQA9O"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izKaF5fRQ-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 15 ‎‎ZYT-00048 (Snapdragon X Elite/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,78,990",
        "rating": "4.7",
        "specScore": "50",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB ‎LPDDR5x RAM",
            "1 TB SSD",
            "Qualcomm Adreno GPU",
            "15 inches, 2496 x 1664 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uIodSjFtFRDrKb9ihrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6c5U6cFFic8Yuis8Fc55ctsnac54cYuAtcTAiciYFBTrIchnc5cbbcOWch-hDZPX4oZhrhhaFhrhrhhacBrWahrhrBi544ibTYU5hrFB5-1OsiEnPEXb9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikTCMgSLR-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 15 ‎ZHG-00023 (Snapdragon X Elite/ 16GB/ 256GB SSD/ Win11)",
        "price": "₹1,39,990",
        "rating": "4.4",
        "specScore": "45",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "12 Cores",
            "16 GB ‎LPDDR5x RAM",
            "256 GB SSD",
            "Qualcomm Adreno GPU",
            "15 inches, 2496 x 1664 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uDDJNnBmfi-1b9J5hrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcaThscUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6co4bW6cFFic8Yuis8Fc55ctsnac54cYuAtcTAiciYFBTrIcBTrUYuCnc5cbbcOWch-hDZPX4oPhrhhaFhrhrhhacBrWahrhrBi53XINQDUshrFB5jCHogX48D~K6"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icP26XxMw-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 7 ‎ZGM-00023 (Snapdragon X Plus/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,31,990",
        "rating": "4.5",
        "specScore": "45",
        "features": [
            "Qualcomm Snapdragon X Plus",
            "10 Cores",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.8 inches, 2304 x 1536 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.u7RlEWRQD-Uu2WbNhrhAA3snrh7nYA3sFsgUcFC3grAacGUtcaiYUh3cNCrTAsnncFurBi3rWsucDcBTCFcUsCAtFA3aaucCTU3rcUtYucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5ZcXcYuAtcTAiciYFBTrIcBTrUYuCnc5cZHcOWch-hDZPX455hrhhaFhrhrhhacBrWahrhrBi5Wi268rD2hrFB56KFynYv.rO-G"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irs121NYp-w280-h280/lenovo-ideapad-1-15i.webp",
        "productName": "Lenovo IdeaPad 1 15IGL7 82V700HRIN Laptop (Celeron N4020/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹25,490",
        "rating": "4.5",
        "specScore": "47",
        "features": [
            "4th Gen Intel Celeron N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0Zi4-gl45j.VN_qhrhAA3snrh7Taus2scYiarBric5c54YWTGcYuUaTcAaTa3sucTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcticiYFBTrIcnFcsggYAacoPo5cATsCicW3aIc5c4HcOWch-hDZPGllXhrhhaFhrhrhhacBrWahrhrBi5ITa3uFHyhrFB5dTPt7_TrwFWH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJLqHVTur-w280-h280/dell-inspiron-7441-p.webp",
        "productName": "Dell Inspiron 7441 Plus AI Laptop (Snapdragon X Plus/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,09,990",
        "rating": "4.15",
        "specScore": "56",
        "features": [
            "Qualcomm Snapdragon X Plus X1P-64-100",
            "10 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "14 inches, 2560 x 1600 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzVUKIfHqSkBe8bhrhArnrysuhyihDRPKXRz547-h-hrhhaFhrhrhhacBrWahrhrBi5gY6CGAIohrFB58A0_1IA4nqjP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9bJyC2vD-w280-h280/dell-xps-13-9345-ai.webp",
        "productName": "Dell XPS 13 9345 AI Laptops (Snapdragon X Plus/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,44,990",
        "rating": "4.5",
        "specScore": "55",
        "features": [
            "Qualcomm Snapdragon X Plus X1E-80-100",
            "12 Cores",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "13.4 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRE~snRJkTgwVHQB88JhrhArnrysuhy6h-usiahk5PPolGl4lPZ5hrhhaFhrhrhhacBrWahrhrBi5P56XnbgihrFB5wb99SPH9Jdkn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXNMKZrn1-w280-h280/hp-chromebook-x360-1.webp",
        "productName": "HP Chromebook x360 14b-cd0014TU Laptop (Intel Core i3-N305/ 8GB/ 256GB UFS/ Chrome OS)",
        "price": "₹50,490",
        "rating": "4.15",
        "specScore": "39",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqV0OGam.JXxjiQhrhArnrysuhyihDRPKbo-0w7zh-hrhhaFhrhrhhacBrWahrhrBi5uBHa4nFyhrFB5it~dBQznA4aO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioXhPbad8-w280-h280/hp-chromebook-x360-1.webp",
        "productName": "HP Chromebook x360 14b-cd0013TU Laptop (Intel Core i3-N305/ 8GB/ 128GB UFS/ Chrome OS)",
        "price": "₹48,247",
        "rating": "4.65",
        "specScore": "39",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFpn6VqBR8mUIaJhrhAgTYBOr3Uh7tBcDZbPcAsuhCUY6TacoYu5cYuUaTcAs3acYZcuZP4cXcW6c5oXcW6cAt3snacBTCFc5H6cAiPP5ZUCcAt3sna6ssOcTrBUshDhDh8g6Hr4iPXbriPrhmBYihkwkpSo04fGKxjep1.hrhhaFhrhrhhacBrWahrhrBi54D4aWCAnhrFB5ZGOiR9wNFqje"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivduWd3fR-w280-h280/hp-omen-16-wf0060tx.webp",
        "productName": "HP Omen 16-wf0060TX Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,71,999",
        "rating": "4.05",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ6KNxu8tHfayRSdhrhArnrysuhyihDRPw__zlfKHh-hrhhaFhrhrhhacBrWahrhrBi5Du3AoW3AhrFB5lgsClq1ej3bG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLyMGa1ZK-w280-h280/dell-g15-5535-gaming.webp",
        "productName": "Dell G15-5535 Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 512GB SSD/ Win11/ RTX 4060 8GB Graph)",
        "price": "₹1,08,990",
        "rating": "4.2",
        "specScore": "74",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGv3tm3fqIEk~4e5hrhAgTYBOr3Uh7iaTTcWrnhNcW54c44Z4crnic3IyaucGcsAUrcAs3acGXHPtFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacXcW3rBtYAFcu2YiYrcWags3Aac3UDcHPbPc5b4ctycTrBUshDhDh86rog5Zb4ZPog6hmBYihkwkpSo-.vjqjKdwbehrhhaFhrhrhhacBrWahrhrBi5to2GIDNWhrFB5_26kpqyXRa2H"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQ0gVgKNr-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 14IRU8 82X6004GIN Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹39,990",
        "rating": "4.35",
        "specScore": "44",
        "features": [
            "13th Gen Intel Core i3 1305U",
            "5 Cores (1P + 4E), 6 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYHB8HtJvyS7JpthrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcAs3acYZc5ZUtcWauc5ZP4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HY3CXcUtYucTYWtUcTrBUshDhDh8A5APrZgA6blrahmBYihkwkpSxf.ZZjKxe._ehrhhaFhrhrhhacBrWahrhrBi5tWFTtDGghrFB5WbqmX9OPppE-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icegQnkCe-w280-h280/lenovo-yoga-pro-7-14.webp",
        "productName": "Lenovo Yoga Pro 7 14IMH9 83E2005EIN Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home/ 6GB Graphics)",
        "price": "₹1,48,990",
        "rating": "4",
        "specScore": "68",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "14.5 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXNSX4iSEx~KypHEVEthrhAgTYBOr3Uh7Taus2scIsWrcB3scGcrYcBAcocXOcsTaicYuUaTcAs3acCTU3rc544tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFc5HYntlcUtYucTYWtUcTrBUshDhDh8ibP44Xo5PGZZXhmBYihkwkpSxbJS00070SzXhrhhaFhrhrhhacBrWahrhrBi58oXaTOT5hrFB5_8qr77YHlSsV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijK2iLw3E-w280-h280/hp-chromebook-14a-nf.webp",
        "productName": "HP Chromebook 14a-nf0014tu Laptop (Intel Processor N100/ 4GB/ 64GB UFS/ Chrome OS)",
        "price": "₹29,990",
        "rating": "4.35",
        "specScore": "34",
        "features": [
            "Intel N100 N100",
            "Quad Core, 4 Threads",
            "4 GB LPDDR5 RAM",
            "64 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqG4Q5J3jF~ppWqhrhArnrysuhyihDRPKboS_mJ1h-hrhhaFhrhrhhacBrWahrhrBi5nbUYQ3NHhrFB5vx0l4H.DNXik"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVzbTqvR7-w280-h280/hp-chromebook-x360-1.webp",
        "productName": "HP Chromebook x360 14b-cd0011TU Laptop (Intel Processor N100/ 4GB/ 128GB UFS/ Chrome OS)",
        "price": "₹36,307",
        "rating": "4.7",
        "specScore": "36",
        "features": [
            "Intel N100 N100",
            "Quad Core, 4 Threads",
            "4 GB LPDDR5 RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD",
            "14 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sF7PW.9e36-DiuWhrhAgTYBOr3Uh7tBcYuUaTcAs3acucu5PPcHcW6c5oXcW6cAt3snacsFc5H6cAiPP55UCcAt3sna6ssOcTrBUshDhDh8raGlG6X46AiiXhmBYihkwkpSo04fd.S-wf7VhrhhaFhrhrhhacBrWahrhrBi5uGaIyBANhrFB5XpVEKHX6ZE9."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iF1ck0DVI-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 ‎15IRU9 83E6001JIN Laptop (Intel Core 5 120U/ 16 GB RAM/ 512GB SSD/ Win 11)",
        "price": "₹64,990",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwni4OiTyjERk9shrhArnrysuhyihDRPKXbJwod1h-hrhhaFhrhrhhacBrWahrhrBi5DO4ObCsrhrFB5wPFSrS_dwXEC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icEfoar5s-w280-h280/gigabyte-g5-mf5-52in.webp",
        "productName": "Gigabyte G5 MF5-52IN354SH Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹91,051",
        "rating": "4.6",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RKoAdzv.wGrXspKhrhArnrysuhyihDRPKZ5v4_ZXh-hrhhaFhrhrhhacBrWahrhrBi5PoD26AalhrFB50wU6fbOYAVNp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDm6d6c0B-w280-h280/gigabyte-g6-mf-h2in8.webp",
        "productName": "Gigabyte G6 MF-H2IN853SH Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 6GB Graph)",
        "price": "₹97,106",
        "rating": "4.35",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RK4pVUnaXjYoBH7hrhArnrysuhyihDRPKZ5dG0m.h-hrhhaFhrhrhhacBrWahrhrBi5BN55GPsahrFB5dPONpfxe23kw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iw58KlAeK-w280-h280/msi-modern-15-h-ai-c.webp",
        "productName": "MSI Modern 15 H AI C1MG-045IN Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹72,990",
        "rating": "4.7",
        "specScore": "60",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw3AG2T3DtN4pY6hrhArnrysuhyihDRPR0JRZ-Hmh-hrhhaFhrhrhhacBrWahrhrBi5BGgilCuyhrFB5.rZD.IbW.x9B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0652l5l6-w280-h280/hp-15s-fy5010tu-lapt.webp",
        "productName": "HP 15s-fy5010TU Laptop (12th Gen Core i3/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹34,990",
        "rating": "4.4",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzaunnUlY1l75BahrhAgTYBOr3Uh7tBcTrBUsBcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6co4bcW6cFFic8Yuis8Fc55ctsnac54FcgI4P5PUCcUtYucTYWtUh-hDh845Zr5Z4igHiZPhmBYihkwkpSxbJjf~J1zxvehrhhaFhrhrhhacBrWahrhrBi5trZ834nuhrFB5KRlGuG7U-Pz7"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iacpTNP7r-w280-h280/gigabyte-g6-kf-h3in8.webp",
        "productName": "Gigabyte G6 KF-H3IN853SH Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,06,495",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzPDCs5P6v.egowhrhArnrysuhyihDRPKZ5-ld.vh-hrhhaFhrhrhhacBrWahrhrBi5yiaAWsNWhrFB5CePPd8q51Nnz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijZZfWpWB-w280-h280/gigabyte-g5-kf5-h3in.webp",
        "productName": "Gigabyte G5 KF5-H3IN353SH Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,06,897",
        "rating": "4.1",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzonAO2Ruz7EW~ThrhArnrysuhyihDRPKZ5~KbJoh-hrhhaFhrhrhhacBrWahrhrBi5W5TUsAHyhrFB5Vxkn3-G0NPyx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixygB1T9E-w280-h280/dell-inspiron-5640-l.webp",
        "productName": "Dell Inspiron 5640 Laptop (Intel Core 5 120U Processor/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹79,290",
        "rating": "4.15",
        "specScore": "55",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwC_a3zKxzHwT2QhrhArnrysuhyihDRPKZml_Rl5h-hrhhaFhrhrhhacBrWahrhrBi52nlgsnguhrFB5Jgwp_S1D_zKo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilpjzUnFy-w280-h280/msi-pulse-17-b13vfk.webp",
        "productName": "MSI Pulse 17 B13VFK-667IN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,27,990",
        "rating": "4.2",
        "specScore": "73",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "17.3 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Hv_bYUX-wFKpz~hrhArnrysuhyihDRPKGp.0mwwh-hrhhaFhrhrhhacBrWahrhrBi5YoPZB45YhrFB5_GPaxwJO2sQI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isEYCXULX-w280-h280/hp-15-fd0123tu-lapto.webp",
        "productName": "HP 15-fd0123TU Laptop (Intel Core i3 N305/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹32,990",
        "rating": "4.55",
        "specScore": "47",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY5gSqJQffyP7s4hrhAgTYBOr3Uh7tBcTrBUsBcYuUaTcAs3acYZcuZP4cXcW6c45ocW6cFFic8Yuis8Fc55ctsnac54cgiP5oZUCcUtYucTYWtUh-hDh8iGlZZbP6XPgAohmBYihkwkpSxbJjVwdexHzphrhhaFhrhrhhacBrWahrhrBi528HCau63hrFB5iEW-Z_ftiqsr"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwtCIEKl3-w280-h280/asus-vivobook-16-x16.webp",
        "productName": "Asus Vivobook 16 X1605ZAC-MB542WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹54,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFvG-Qp~0YjGo0ohrhAgTYBOr3Uh7rFCFcYuUaTcAs3acY4c5oUtcWauc5o4PPtc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacD5bP4yrAcn64Ho8FcTrBUshDhDh85XXi6igPoXiZPhmBYihkwkpSoGH0evSG7SpdhrhhaFhrhrhhacBrWahrhrBi5FXiaZnyohrFB5-SWrOP1U1xgO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icPF8XPJy-w280-h280/msi-crosshair-16-hx.webp",
        "productName": "MSI Crosshair 16 HX Monster Hunter Edition D14VFKG-408IN Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB RTX4060)",
        "price": "₹1,67,990",
        "rating": "4.4",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMSI%2520Crosshair%252016%2520HX%2520Monster%2520Hunter%2520Edition%2520D14VFKG-408IN%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i7%252F%252016GB%252F%25201TB%2520SSD%252F%2520Win11%252F%25208GB%2520RTX4060)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iX0GM9WcY-w280-h280/lenovo-ideapad-5i-83.webp",
        "productName": "Lenovo IdeaPad 5i 83DT004SIN Laptop (Intel Core 5 120U/ 16 GB RAM/ 512GB SSD/ Win 11)",
        "price": "₹79,990",
        "rating": "4.7",
        "specScore": "62",
        "features": [
            "Intel Core 5 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Integrated Intel",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYekBzXJJSe2Ju_hrhAgTYBOr3Uh7Taus2scYiarBric4cocYuc5cYuUaTcAs3ac5oPCc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac5HY3Clcoc5cTrBUshDhDh84G5AaGlAAoPgihmBYihkwkpSf0.e7.1Vwdx.hrhhaFhrhrhhacBrWahrhrBi5gaHrDGgihrFB5Q0wnoTg4siXY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaN5jOwsc-w280-h280/hp-pavilion-aero-202.webp",
        "productName": "HP Pavilion Aero 2024 Laptop (Intel Core Ultra 7 155U/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹99,990",
        "rating": "4.1",
        "specScore": "55",
        "features": [
            "Intel Core Ultra 7 155U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "13.3 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520Pavilion%2520Aero%25202024%2520Laptop%2520(Intel%2520Core%2520Ultra%25207%2520155U%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win%252011%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieoCrB5TP-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1504VA-NJ540WS Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹54,990",
        "rating": "4.6",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwWQ3Co5zbBzpJKhrhArnrysuhyihDRPKHz7.75Sh-hrhhaFhrhrhhacBrWahrhrBi5y5QBCDyHhrFB5E4uBdYE0B23_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifDjOkWmU-w280-h280/hp-spectre-x360-16-a.webp",
        "productName": "HP Spectre x360 16-aa0015TU Laptop ( Intel Evo Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,56,990",
        "rating": "4.05",
        "specScore": "74",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5x RAM RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2560 x 1600 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ.qGH-aJ3IjpCqGhrhArnrysuhyihDRPKbvGb4llh-hrhhaFhrhrhhacBrWahrhrBi5XioggCWWhrFB5S2Ott5UDdsHn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipBQ1DMWB-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Ultra NP960XGL-XG1IN Laptop (Intel Core Ultra 7 155H/ 16GB RAM/ 1TB SSD/ 6 GB Graphics)",
        "price": "₹2,23,990",
        "rating": "4.75",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJHaf7.ziWyu3Pu_XOBhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcCTU3rc5bcYuAtcCTU3rcGc5bW6c5U6cuBlbPDWTcDW5Yuh-hrhhaFhrhrhhacBrWahrhrBi5CA6FiZBUhrFB5l.XJ~X2O-RU-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4O9SXIob-w280-h280/hp-victus-15-fa1333t.webp",
        "productName": "HP Victus 15-fa1333TX Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graphics RTX 4060)",
        "price": "₹1,08,531",
        "rating": "4.05",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_ooxmg7foNvOl~YhrhArnrysuhyihDRPKGS54el.h-hrhhaFhrhrhhacBrWahrhrBi5gu2CnsDrhrFB5HrQ-TOs1dkPF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOyDwp5Uc-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 UN.343SI.00A Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹52,990",
        "rating": "4.2",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB  RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYKvY2OqrYHBn50hrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8Gaao5aoiG5GZXhmBYihkwkpSfoHvRpj.xVx_hrhhaFhrhrhhacBrWahrhrBi5tsY43WFyhrFB5xa1iU1CfDw6e"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOyDwp5Uc-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 UN.343SI.004 Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹49,990",
        "rating": "4.75",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjQl2-7IZBR7I1hrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8X4X6XZglPH4lZhmBYihkwkpSfoHvxbVfSKvqhrhhaFhrhrhhacBrWahrhrBi5GXOt5438hrFB5Yoqx-or.kqPW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilStnR7Dn-w280-h280/lenovo-loq-15iax9i-8.webp",
        "productName": "Lenovo LOQ 15IAX9I 83FQ000EIN Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹58,490",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Intel Arc A530M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0Z8G7YRsdYVCmFChrhAA3snrh7Taus2scTsNc54YrDlYcYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnacHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticYBFciYFBTrIcYuUaTcr3Acr4ZPncnFcsggYAacZb4cTCurcW3aIcocZXcOWch-hDZP4bXHhrhhaFhrhrhhacBrWahrhrBi5O24bsBP4hrFB548TPZKZrxaDz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGFTZRQUL-w280-h280/msi-modern-15-h-b13m.webp",
        "productName": "MSI Modern 15 H B13M-224IN Laptop (13th Gen Core i9/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹76,990",
        "rating": "4.6",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0HGjVgIIrCUC1g7hrhAA3snrh7nFYcnsia3uc54cYuUaTcAs3acYlc5ZUtcWaucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5cATrFFYAchnc5clcOWch-hDZPbbb4hrhhaFhrhrhhacBrWahrhrBi5aIG8UXXYhrFB5dRgX2w07a~w_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGDVR7fSQ-w280-h280/msi-cyborg-15-ai-a1v.webp",
        "productName": "MSI Cyborg 15 AI A1VEK-096IN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,10,990",
        "rating": "4.4",
        "specScore": "71",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ808afjdxRIfboYCWA7hrhAA3snrh7nFYcAI6s3Wc54cYuUaTcAs3acCTU3rcGc5FUcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcHP4PcnFcsggYAacoPo5cU3ruFTCAauUchnc5clXcOWch-hDZPbbbHhrhhaFhrhrhhacBrWahrhrBi5Ps86DbnThrFB59EpYIO3djIzU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXZdA8MFL-w280-h280/msi-modern-15-h-b13m.webp",
        "productName": "MSI Modern 15 H B13M-225IN Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹66,990",
        "rating": "4.75",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0H5SbBdqHNmygZfhrhAA3snrh7nFYcnsia3uc54cYuUaTcAs3acYGc5ZUtcWaucTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac54cbcYuAtcgCTTcticiYFBTrIcnFcsggYAacoPo5cATrFFYAchnc5clcOWch-hDZPbbbbhrhhaFhrhrhhacBrWahrhrBi5PNWOrYrYhrFB5WIvyobdC7wSq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuxfwlvGo-w280-h280/lenovo-ideapad-pro-5.webp",
        "productName": "Lenovo IdeaPad Pro 5 83D5000SIN Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 1TB SSD/ Win11/ RTX 4050 6GB Graphics)",
        "price": "₹1,29,990",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Integrated Intel Arc Graphics",
            "16 inches, 2048 x 1280 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ0sZ52knqCvfCC4hrhArnrysuhyihDRPwJ4JVvozh-hrhhaFhrhrhhacBrWahrhrBi52uBlgZXrhrFB5rUEGH~zK.jd1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXUSWnAWR-w280-h280/msi-cyborg-15-a13vfk.webp",
        "productName": "MSI Cyborg 15 A13VFK-1079IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,04,990",
        "rating": "4.45",
        "specScore": "70",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ808a_-pqrC68SJPn~ohrhAA3snrh7nFYcAI6s3Wc54cYuUaTcAs3acYGc5ZUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacXW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcHPbPcnFcsggYAacoPo5cU3ruFTCAauUchnc5clXcOWch-hDZPbbbZhrhhaFhrhrhhacBrWahrhrBi5YW8HtYIIhrFB56IWZvwdEkmUG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0fCwT13g-w280-h280/msi-katana-a15-ai-b8.webp",
        "productName": "MSI Katana A15 AI B8VF-447IN Gaming Laptop (AMD Ryzen 9 8945HS/ 16GB/ 512GB SSD/ Win11 /8GB Graph)",
        "price": "₹1,24,990",
        "rating": "4.25",
        "specScore": "77",
        "features": [
            "8th Gen AMD Ryzen 9 8945HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1080 x 1920 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ808a.nJo_T-82v8DKXhrhAA3snrh7nFYcOrUrurcr54crnic3IyauclcXUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacXW6cW3rBtYAFc54cbcYuAtc5HHctycgticiYFBTrIcu2YiYrcWags3Aac3UDcHPbPcnFcsggYAacoPo5chncoco4cOWch-hDZPbbbohrhhaFhrhrhhacBrWahrhrBi5ZGF66YWlhrFB5ICYSU8KH6Nzm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC0zrxgIN-w280-h280/dell-xps-16-9640-ole.webp",
        "productName": "Dell XPS 16 9640 OLED Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11/ RTX 4060 8GB Graphics)",
        "price": "₹3,15,090",
        "rating": "4.75",
        "specScore": "86",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.3 inches, 3840 x 2400 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREv_PqF31w-r~UzXoUhrhArnrysuhyihDRPKoK1XXefh-hrhhaFhrhrhhacBrWahrhrBi53PrYaTWahrFB57Ibo2QdUiyTZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTzDrDMbR-w280-h280/msi-modern-15-h-ai-c.webp",
        "productName": "MSI Modern 15 H AI C1MG-049IN Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹73,990",
        "rating": "4.65",
        "specScore": "57",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwFHKT0tqzFtzJbhrhArnrysuhyihDRPKZJbJz1Jh-hrhhaFhrhrhhacBrWahrhrBi5FbHWCrGthrFB5TpuG5bj3GEYb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKDkEpTsa-w280-h280/msi-modern-15-h-ai-c.webp",
        "productName": "MSI Modern 15 H AI C1MG-048IN Laptop (Intel Core Ultra 7 155H/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹72,990",
        "rating": "4.5",
        "specScore": "59",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw3AG2T3DW8FiUEhrhArnrysuhyihDRPKZJSXd-mh-hrhhaFhrhrhhacBrWahrhrBi5PNlOatHChrFB5r40X5DJ-d.HA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAOXCsBtx-w280-h280/lenovo-yoga-7-14irl8.webp",
        "productName": "Lenovo Yoga 7 14IRL8 OLED 82YL0096IN Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,14,990",
        "rating": "4.25",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJEb5PQ7U2k5OOKahrhArnrysuhyihDRPK5x.HHp-h-hrhhaFhrhrhhacBrWahrhrBi5ItTHB6BbhrFB5l4qkbpZuDsWP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iO8XBpUEC-w280-h280/msi-katana-a17-ai-b8.webp",
        "productName": "MSI Katana A17 AI B8VG-868IN Gaming Laptop (AMD Ryzen 9 8945HS/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,46,990",
        "rating": "4.2",
        "specScore": "78",
        "features": [
            "8th Gen AMD Ryzen 9 8945HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "17.3 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_bsuWBkQ3KGkmO2hrhArnrysuhyihDRPw0~1GJwHh-hrhhaFhrhrhhacBrWahrhrBi5OglUusFahrFB5CNgq5NdU_DUq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMy0EduyA-w280-h280/msi-katana-a15-ai-b8.webp",
        "productName": "MSI Katana A15 AI B8VG-440IN Gaming Laptop (AMD Ryzen 9 8945HS/ 16GB/ 1TB SSD/ Win11 /8GB RTX 4070 Graph)",
        "price": "₹1,43,990",
        "rating": "4.3",
        "specScore": "78",
        "features": [
            "8th Gen AMD Ryzen 9 8945HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "15.6 inches, 1080 x 1920 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ_t3Esw3zYqUe6YhrhArnrysuhyihDRPw0~dlV4Kh-hrhhaFhrhrhhacBrWahrhrBi5IaNu5TZohrFB50yFJGypFSlwt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAWV4bUsE-w280-h280/dell-9440-xps-14-lap.webp",
        "productName": "Dell 9440 XPS 14 Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11/ RTX 4050 6GB Graphics)",
        "price": "₹2,47,990",
        "rating": "4.45",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "14.5 inches, 3200 x 2000 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJsXDG34UkzeT3H7hrhArnrysuhyihDRPKoK~lzH_h-hrhhaFhrhrhhacBrWahrhrBi555naTliAhrFB5GSryaPs2b78j"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idrFr4ePf-w280-h280/dell-xps-14-9440-lap.webp",
        "productName": "Dell XPS 14 9440 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹2,02,390",
        "rating": "4.35",
        "specScore": "73",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Arc graphics",
            "14.5 inches, 3200 x 2000 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJYWeBQdgTyPFD6xhrhArnrysuhyihDRPKoK1oR~vh-hrhhaFhrhrhhacBrWahrhrBi5irQA8PrUhrFB5Yuz1YB-eNTNm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYw7a1pYM-w280-h280/msi-summit-16-ai-evo.webp",
        "productName": "MSI Summit 16 AI Evo A1MTG-025IN Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,37,990",
        "rating": "4.4",
        "specScore": "72",
        "features": [
            "1st Gen Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2560 x 1600 pixels, Touch Screen",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBVZFWs~YtqTlR3vhrhArnrysuhyihDRPKoSf.1x1h-hrhhaFhrhrhhacBrWahrhrBi5NOngstCAhrFB5YFu8dAw.TqgT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iumjMrNVk-w280-h280/msi-thin-15-b13ucx-1.webp",
        "productName": "MSI Thin 15 B13UCX-1808IN Gaming Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 4GB RTX 2050 Graph)",
        "price": "₹53,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI9J4DjDs6ItlwGhrhArnrysuhyihDRPw0l-_1R4h-hrhhaFhrhrhhacBrWahrhrBi5alFI5iGAhrFB5syitmyWXVQBn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieZhVys07-w280-h280/msi-stealth-18-ai-st.webp",
        "productName": "MSI Stealth 18 AI Studio A1VHG-023IN Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 2TB SSD/ Win11 Home/ 12GB RTX 4080 Graph)",
        "price": "₹3,40,990",
        "rating": "4.45",
        "specScore": "93",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Ap0Bb1mKOGymxthrhArnrysuhyihDRPw_K-pV~oh-hrhhaFhrhrhhacBrWahrhrBi5olW5YODthrFB5GJT-voSA.7El"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIdE2tbuc-w280-h280/hp-elitebook-ultra-a.webp",
        "productName": "HP EliteBook Ultra AI PC Laptop (Snapdragon X Elite / 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,69,990",
        "rating": "4.35",
        "specScore": "46",
        "features": [
            "Qualcomm Snapdragon X Elite",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Qualcomm Adreno GPU",
            "14 inches, 2240 x 1400 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520EliteBook%2520Ultra%2520AI%2520PC%2520Laptop%2520(Snapdragon%2520X%2520Elite%2520%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikY1ync4K-w280-h280/gigabyte-aorus-16x-a.webp",
        "productName": "Gigabyte Aorus 16X ASG-63USC65SH Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,89,990",
        "rating": "4",
        "specScore": "86",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DGigabyte%2520Aorus%252016X%2520ASG-63USC65SH%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25202TB%2520SSD%252F%2520Win11%2520Home%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iG6wvY8eg-w280-h280/hp-envy-x360-15-fh00.webp",
        "productName": "HP Envy x360 15-fh0032AU Laptop (AMD Ryzen 7 7730U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹79,490",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "7th Gen AMD Ryzen 7 7730U",
            "Octa Core, 16 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwC6IBUmX0WOBFXhrhArnrysuhyihDRPKobb-xbvh-hrhhaFhrhrhhacBrWahrhrBi54Bgyo3N5hrFB50Vt~_w5~nUet"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9RYMQDLu-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JRS00D00 Laptop (AMD Ryzen 5 7530U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹53,499",
        "rating": "4",
        "specScore": "63",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwWG47i~HrlBE.vhrhArnrysuhyihDRPwJv.ww-fh-hrhhaFhrhrhhacBrWahrhrBi52sGZFUuOhrFB5DJ9WRNHZG.wT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAPZbxPhp-w280-h280/dell-xps-13-9315-lap.webp",
        "productName": "Dell XPS 13 9315 Laptop (12th Gen Core i7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,66,790",
        "rating": "4.5",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i7 1250U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "13.4 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJrvnnAiubDYWafYhrhArnrysuhyihDRPwd.X1JeXh-hrhhaFhrhrhhacBrWahrhrBi52UB833aYhrFB5.tuk_l~wbkwt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iiFZNMXXX-w280-h280/acer-chromebook-plus.webp",
        "productName": "Acer Chromebook Plus 515 CB515-2H ‎NX.KNUSI.002 Laptop (13th Gen Core i3 1315U/ 8GB/ 256GB SSD/ Chrome OS)",
        "price": "₹34,990",
        "rating": "4.05",
        "specScore": "46",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB  RAM",
            "256 GB SSD",
            "Intel Integarted Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQYVJkimPqy5P4uhrhAgTYBOr3Uh7rAa3cAt3sna6ssOcBTCFcoPoHcYuUaTcAs3acYZc5ZUtcWauc5Z54CcXcW6co4bcW6cFFicAt3snacsFcTrBUshDhDh86ZXbb5AXgGg65hmBYihkwkpSxwlVfXjS7fKZhrhhaFhrhrhhacBrWahrhrBi5HB2Yr8a6hrFB5J5sJGFzrzzmd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYvgvcAnt-w280-h280/hp-victus-15-fa1310t.webp",
        "productName": "HP Victus 15-FA1310TX Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB RTX 2050)",
        "price": "₹54,999",
        "rating": "4.4",
        "specScore": "63",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZCzsvWpA4_1YbahrhAA3snrh7tBc2YAUCFc54cgr5Z5PUDcYuUaTcAs3acY4c5oUtcWaucWrnhNcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55cHW6cW3rBtYAFc54cbcYuAtc5HHctycgCTTcticiYFBTrIcu2YiYrcWags3Aac3UDcoP4PcnFcsggYAacBa3gs3nruAac6TCacocZGcOWch-hDZPG5oohrhhaFhrhrhhacBrWahrhrBi5nArFNCryhrFB5T6m4XKYDlqFU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6DEjtfpN-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 UN.343SI.009 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹39,990",
        "rating": "4.15",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYHB8HtJvyS7JpthrhAgTYBOr3Uh7rAa3crFBY3acZc6huTYUcYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8oXirXgbAog45ohmBYihkwkpSfoHvXzeJfe01hrhhaFhrhrhhacBrWahrhrBi5nAOQGrlDhrFB5k1.QfX98o6ZA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iItkUunWj-w280-h280/msi-stealth-18-ai-st.webp",
        "productName": "MSI Stealth 18 AI Studio A1VIG-022IN Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 2TB SSD/ Win11 Home/ 16GB RTX 4090 Graph)",
        "price": "₹3,90,990",
        "rating": "4.45",
        "specScore": "95",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREv_lYXsEpfxuoN66HhrhArnrysuhyihDRPw_K~Sv5fh-hrhhaFhrhrhhacBrWahrhrBi5WDAuQIXXhrFB5G-.I5r8Wbi7F"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iU8IYuvli-w280-h280/lenovo-loq-2024-15ir.webp",
        "productName": "Lenovo LOQ 2024 15IRX9 83DV00LWIN Gaming Laptop (13th Gen Core i7/ 24GB/ 512GB SSD/ Win11/ 6GB RTX4050)",
        "price": "₹1,02,990",
        "rating": "4.5",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "24 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv76g74.0In6GI~4RmohrhAgTYBOr3Uh7Taus2scTsNcYuUaTcAs3acYGc5ZUtcWauc5Zb4PtDcoHcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc54Y3DlcWrnhNcTrBUshDhDh8X6lgoPrAZGHZlhmBYihkwkpSf_0l_Vjf~xRXhrhhaFhrhrhhacBrWahrhrBi5CGbDCtgnhrFB5~ywbw0IAWSqn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iHkkcYnun-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 np750xgk-lg3in Laptop (Intel Core 7 Processor 150U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹79,999",
        "rating": "4.55",
        "specScore": "56",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125EdUBvokqCtCUqjjIlT5BAsZhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHc54cbcYuAtcAs3acGc5bW6c45oW6cuBG4PDWOcTWZYuh-hrhhaFhrhrhhacBrWahrhrBi5oy4Wl4G6hrFB5snNKKNmz0d~b"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFirLuVot-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro NP960XGK-LG3IN Laptop (Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,76,990",
        "rating": "4.5",
        "specScore": "74",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJHafbIJ4~ASwpX4HyRhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3sc5bcYuAtcCTU3rcGcZoW6c5U6cuBlbPDWOcTWZYuh-hrhhaFhrhrhhacBrWahrhrBi56Y2tFr6ZhrFB56o.aZu1Q7wgm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieyvGq0yy-w280-h280/acer-chromebook-plus.webp",
        "productName": "Acer Chromebook Plus 514 CB514-4H ‎NX.KUTSI.002 Laptop (Intel Core i3-N305/ 8GB/ 256GB SSD/ Chrome OS)",
        "price": "₹24,990",
        "rating": "4",
        "specScore": "33",
        "features": [
            "Intel Core i3 N305",
            "Octa Core, 8 Threads",
            "8 GB  RAM",
            "256 GB SSD",
            "Intel Integarted Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzfCf8S1wV6mSK8hrhAgTYBOr3Uh7rAa3cAt3sna6ssOcBTCFcoPoHcYuUaTcAs3acYZcuZP4cXcW6co4bcW6cFFicAt3snacsFcA645HcHtcZlUGcTrBUshDhDh844HoAAblPPaA5hmBYihkwkpSxwlVqZlJ7SpjhrhhaFhrhrhhacBrWahrhrBi5HTCWrDZPhrFB5qZ1wzkTrJf6R"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBEh6v1j7-w280-h280/hp-victus-15-fa1332t.webp",
        "productName": "HP Victus 15-fa1332tx Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ RTX 4050)",
        "price": "₹1,01,990",
        "rating": "4.35",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_515DtyuJYugCFNhrhArnrysuhyihDRPKoKSdVxRh-hrhhaFhrhrhhacBrWahrhrBi5G35bFn6HhrFB50CuuKN0bXiYl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipX28hyqM-w280-h280/asus-tuf-gaming-a16.webp",
        "productName": "Asus TUF Gaming A16 2024 Gaming Laptop (AMD Ryzen 9 AI HX 370/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,99,990",
        "rating": "4.25",
        "specScore": "62",
        "features": [
            "AMD Ryzen 9 AI HX 370",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520TUF%2520Gaming%2520A16%25202024%2520Gaming%2520Laptop%2520(AMD%2520Ryzen%25209%2520AI%2520HX%2520370%252F%252016GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikTN8ABkV-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus Vivobook 15 X1504ZA-NJ540WS Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹48,990",
        "rating": "4.6",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjSH4.vtSn.JeUhrhAgTYBOr3Uh7rFCFc2Y2s6ssOc54c6huTYUcOaI6sr3icYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacD54PHyrcuQ4HP8FcUtYucTYWtUcTrBUshDhDh84bGaHlgHHgZllhmBYihkwkpSf7X.e1lKwo7.hrhhaFhrhrhhacBrWahrhrBi5XAUNala5hrFB5baU~xQUWKO.B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iv0oRgUsR-w280-h280/acer-aspire-3-a324-5.webp",
        "productName": "Acer Aspire 3 A324-51 UN.343SI.006 Laptop (12th Gen Core i3/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹27,990",
        "rating": "4.25",
        "specScore": "50",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtIoJfAGkpaX7QDhrhAgTYBOr3Uh7rAa3crFBY3acZcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacrZoHc45cUtYucTYWtUcTrBUshDhDh8HiAirAGAboGgXhmBYihkwkpSfoHvHed~J.7.hrhhaFhrhrhhacBrWahrhrBi53rYGHBN5hrFB5rCwxmrVp3fgH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSex4yI0k-w280-h280/hp-envy-x360-15-fh00.webp",
        "productName": "HP Envy x360 15-fh0031AU Laptop (AMD Ryzen 5 7530U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹67,990",
        "rating": "4.05",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwuydx3xuEAPiBphrhArnrysuhyihDRPK54ZfGfHh-hrhhaFhrhrhhacBrWahrhrBi5l3TW2n2UhrFB5iwv7q0BQHmXk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0HpBgXYv-w280-h280/dell-alienware-m16-r.webp",
        "productName": "Dell Alienware M16 R1 ANM16I7CDG7001ODB1 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win 11/ 6GB Graph)",
        "price": "₹1,45,990",
        "rating": "4.6",
        "specScore": "75",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_bYCeyZik.~AvgphrhArnrysuhyihDRPwlx4pVeGh-hrhhaFhrhrhhacBrWahrhrBi5PBY5BQHWhrFB5q4inlP-0yrsv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i21ZTLWUt-w280-h280/lenovo-loq-2024-15ah.webp",
        "productName": "Lenovo LOQ 2024 ‎15AHP9 83DX0006IN Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹99,990",
        "rating": "4.35",
        "specScore": "73",
        "features": [
            "8th Gen AMD Ryzen 7 8845HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrO-8VaIIefzf7SihrhAgTYBOr3Uh7Taus2scTsNcrnic3IyaucGcsAUrcAs3acXXH4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc54rtBlcWrnhNcTrBUshDhDh8PbGXg5HGb554ihmBYihkwkpSxo-f7KEXSpxqhrhhaFhrhrhhacBrWahrhrBi5PaoPW8NUhrFB5WRqjzRGKtlvk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iteUtNDjq-w280-h280/asus-expertbook-b1-b.webp",
        "productName": "Asus ExpertBook B1 B1402CBA-NK1494WS Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹36,990",
        "rating": "4.45",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYZza.Eoiglv7NlhrhAgTYBOr3Uh7rFCFcaDBa3U6ssOc65HcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac65HPoA6rcuO5HlH8FcUtYucTYWtUcTrBUshDhDh8blAHAb6bg45PZhmBYihkwkp7.xlqfEfw4oRShrhhaFhrhrhhacBrWahrhrBi5ilUrNyF6hrFB5lSTeDCIJHtJb"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikClD6Ta0-w280-h280/acer-al15g-52-gaming.webp",
        "productName": "Acer ‎AL15G- 52 Gaming Laptop (12th Gen Core i5-12450H/ 16GB/ 1TB SSD/ Win11/ 6GB RTX 3050 Graphics)",
        "price": "₹65,990",
        "rating": "4",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwu4Rrd6xD~PK2~hrhArnrysuhyihDRPKZo~vzZmh-hrhhaFhrhrhhacBrWahrhrBi5GIQgNIY4hrFB5HYp9pmpOW4B~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihVZDo1T9-w280-h280/asus-vivobook-s-15-o.webp",
        "productName": "Asus Vivobook S 15 OLED 2024 S5506MA-MA752WS Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,11,990",
        "rating": "4.45",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Arc",
            "15.6 inches, 2880 x 1620 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGevoW2r3OV_5px0hrhAgTYBOr3Uh7rFCFc2Y2s6ssOcFc54csTaicoPoHcrYcBs8ahBcYuUaTca2sctcFa3YaFcAs3acCTU3rcGc544tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacF44PbnrcnrG4o8FcUtYucTYWtUcTrBUshDhDh8oo6AgiP6bHPlAhmBYihkwkpSff.dVpqp_SKZhrhhaFhrhrhhacBrWahrhrBi5tCIIgBWHhrFB5EWdNdNP1NBAB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGXa1xqbZ-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15 B12MO-817IN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹40,990",
        "rating": "4.65",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqquVK4CnZXYz6yhrhArnrysuhyihDRPK50VZS~Gh-hrhhaFhrhrhhacBrWahrhrBi5iyQWrraohrFB50HNtRmJeD-js"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGXa1xqbZ-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15 B12MO-818IN Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹37,990",
        "rating": "4.7",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQQWuUNss.bNxAmhrhAgTYBOr3Uh7nFYcnsia3uc54cYuUaTcAs3acY4c5oUtcWauc5oZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac65onscX5XYucUtYucTYWtUcTrBUshDhDh8obaHobPXii4oHhmBYihkwkp7fex7xpZ-zS.7hrhhaFhrhrhhacBrWahrhrBi5Fi23OBs6hrFB5m3nlIBZbX2OY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igLbW0aJZ-w280-h280/msi-summit-e13-ai-ev.webp",
        "productName": "MSI Summit E13 AI Evo A1MTG-041IN 2 in 1 Laptop Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,47,990",
        "rating": "4.2",
        "specScore": "68",
        "features": [
            "1st Gen Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Intel Arc",
            "13.3 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBm9ern3HtfQGSxyhrhArnrysuhyihDRPKZm.w7Slh-hrhhaFhrhrhhacBrWahrhrBi5sFaPPa56hrFB5pYbk_KK8WkWn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGXa1xqbZ-w280-h280/msi-modern-15-b12mo.webp",
        "productName": "MSI Modern 15 B12MO-816IN Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹52,990",
        "rating": "4.4",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzBWosiPKPlFooohrhAgTYBOr3Uh7nFYcnsia3uc54cYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac65onscX5bYucUtYucTYWtUcTrBUshDhDh8AHPPZX6PllZZ5hmBYihkwkp7fex7flj_R--dhrhhaFhrhrhhacBrWahrhrBi5QNnXPATshrFB5UBo4tIqQrz01"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idSWO0vc8-w280-h280/asus-vivobook-s-14-o.webp",
        "productName": "Asus Vivobook S 14 OLED 2024 M5406NA-QD551WS Laptop (AMD Ryzen 5 7535HS/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹89,990",
        "rating": "4.05",
        "specScore": "61",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIACV0vjyET9AUehrhArnrysuhyihDRPKZm0-7p~h-hrhhaFhrhrhhacBrWahrhrBi548oXFBrXhrFB5jr50kP07_Xzd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i48V5WrPc-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro 11 2024 Laptop (Snapdragon X Plus/ 16GB/ 256GB SSD/ Win11)",
        "price": "₹1,13,990",
        "rating": "4.4",
        "specScore": "47",
        "features": [
            "Qualcomm Snapdragon X Plus",
            "10 Cores",
            "16 GB LPDDR5x RAM",
            "256 GB SSD",
            "Qualcomm Adreno GPU",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.sgWb.DtVyzG16b2IhrhAA3snrh7nYA3sFsgUcFC3grAacB3sc55UtcaiYUh3c8YcgYc8Yuis8Fc55ctsnacUr6TaUc5ZcYuAtc5bW6c3rnco4bW6c3sncBTrUYuCnch-hDZPX45XhrhhaFhrhrhhacBrWahrhrBi54b5iXPl8hrFB5nxTbWCIY.5HY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTXxujy9r-w280-h280/asus-vivobook-s-16-o.webp",
        "productName": "Asus Vivobook S 16 OLED 2024 S5606MA-MX751WS Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,26,990",
        "rating": "4.45",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB9Q1fyg7qSb1CD9hrhArnrysuhyihDRPlzl11Zzdh-hrhhaFhrhrhhacBrWahrhrBi5AYAl2tOahrFB5oBEB5KNKngaX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGE0ZMnr2-w280-h280/msi-summit-e13-ai-ev.webp",
        "productName": "MSI Summit E13 AI Evo A1MTG-040IN Laptop ( Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,32,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "1st Gen Intel Core Ultra 5 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Intel Arc",
            "13.3 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB-r~.rQwko--e3_hrhArnrysuhyihDRPKZmflpm0h-hrhhaFhrhrhhacBrWahrhrBi5B8ATs8IWhrFB59y1eZtymBDD0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iudDRGiwm-w280-h280/msi-prestige-14-ai-s.webp",
        "productName": "MSI Prestige 14 AI Studio C1UDXG-030IN Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11 Home/ 6 GB Graphics)",
        "price": "₹1,27,990",
        "rating": "4.75",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Hv_bYUX-wFKpz~hrhArnrysuhyihDRPKoSffxJZh-hrhhaFhrhrhhacBrWahrhrBi5Pn4TFWFuhrFB5WP2Aoo5HH9QQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAMFCdpX6-w280-h280/lenovo-yoga-7-14arp8.webp",
        "productName": "Lenovo Yoga 7 14ARP8 82YM0075IN Laptop (AMD Ryzen 7 7735U/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹94,690",
        "rating": "4.1",
        "specScore": "73",
        "features": [
            "7th Gen AMD Ryzen 7 7735U",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Integrated AMD Radeon 680M Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEqoiCCeySECCXVhrhAgTYBOr3Uh7Taus2scIsWrcGcsTaicrnic3IyaucsAUrcAs3acGGZ4Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5Hr3BXcUtYucTYWtUcTrBUshDhDh8ogZgHaiXZiX4ahmBYihkwkpSfl.X7d.jSS77hrhhaFhrhrhhacBrWahrhrBi5uAA6ntF6hrFB5KBueo_Q~gpCN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8DDoSnYt-w280-h280/hp-zbook-power-g10-8.webp",
        "productName": "HP ZBook Power G10 8L147PA Laptop (13th Gen Core i9/ 32 GB/ 1TB SSD/ Win11/ 8GB Graphics)",
        "price": "₹2,84,990",
        "rating": "4.1",
        "specScore": "90",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA RTX 3000 Ada",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520ZBook%2520Power%2520G10%25208L147PA%2520Laptop%2520(13th%2520Gen%2520Core%2520i9%252F%252032%2520GB%252F%25201TB%2520SSD%252F%2520Win11%252F%25208GB%2520Graphics)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZMBmqFUR-w280-h280/dell-inspiron-3535-l.webp",
        "productName": "Dell Inspiron 3535 Laptop (AMD Ryzen R7 5700U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹49,990",
        "rating": "4.15",
        "specScore": "56",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZNN8idw35dy1pWhrhAA3snrh7iaTTcYuFBY3sucZ4Z4crnic3IyaucGc4UtcWaucusUa6ssOcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55c54cbcYuAtcgCTTcticTaic6huTYUciYFBTrIcnFcsggYAacoPo5cAr36suchnc5cbocOWch-hDZP4GGohrhhaFhrhrhhacBrWahrhrBi5PXnQZXFnhrFB5aV9Sz1TY~kdx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iw5nDw0Yt-w280-h280/hp-omen-16-wf0148tx.webp",
        "productName": "HP Omen 16-wf0148TX Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,55,990",
        "rating": "4",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9B2jJ.fTnnRGOj03hrhArnrysuhyihDRPKoKK-51dh-hrhhaFhrhrhhacBrWahrhrBi53h86A5BhrFB5NPrmrAIF7bOC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOcnXVdrE-w280-h280/infinix-inbook-x3-sl.webp",
        "productName": "Infinix INBook X3 Slim XL422 Laptop (12th Gen Core i7/ 32GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹49,990",
        "rating": "4.7",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "32 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjQl2-7IZBR7I1hrhAgTYBOr3Uh7YugYuYDcYuUaTcAs3acYGc5o44CcZocW6c45ocW6cFFic8Yuis8Fc55ctsnacDTHoocUtYucTYWtUcTrBUshDhDh8ZblllAgH6lg5ghmBYihkwkp7z7x7efqGex_.hrhhaFhrhrhhacBrWahrhrBi55WZCrrBXhrFB5RfI3OKSPYK31"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNPRH6Zwb-w280-h280/msi-thin-15-b12ve-16.webp",
        "productName": "MSI Thin 15 B12VE-1689IN Gaming Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 6GB RTX4050 Graph)",
        "price": "₹69,990",
        "rating": "4.15",
        "specScore": "70",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIvGFsKgDmgzGWohrhArnrysuhyihDRPw0lR0vzoh-hrhhaFhrhrhhacBrWahrhrBi5lrUs4U3FhrFB5_~QoEGKs1I9Z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inCqAgPfA-w280-h280/dell-inspiron-5440-l.webp",
        "productName": "Dell Inspiron 5440 Laptop (Intel Core 7 150U Processor/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹87,719",
        "rating": "4.35",
        "specScore": "56",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwyWSa2Xbyzgu4ihrhArnrysuhyihDRPKRm7XxRfh-hrhhaFhrhrhhacBrWahrhrBi5ZPlUgXBlhrFB5wqbRRYJ.V6Y_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIQiwk80X-w280-h280/msi-stealth-14-ai-st.webp",
        "productName": "MSI Stealth 14 AI Studio A1VFG-053IN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home/ 8GB RTX 4060 Graph)",
        "price": "₹1,85,990",
        "rating": "4.25",
        "specScore": "77",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB~oyOyFSu.KeU_PhrhArnrysuhyihDRPKoomRd~0h-hrhhaFhrhrhhacBrWahrhrBi5otBGlagnhrFB5p8.1NJPeHZ0o"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inCqAgPfA-w280-h280/dell-inspiron-5440-l.webp",
        "productName": "Dell Inspiron 5440 Laptop (Intel Core 7 150U Processor/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹87,719",
        "rating": "4.35",
        "specScore": "56",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwyWSa2Xbyzgu4ihrhArnrysuhyihDRPKRm7XxRfh-hrhhaFhrhrhhacBrWahrhrBi5ZPlUgXBlhrFB5wqbRRYJ.V6Y_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izg8cc3x8-w280-h280/lenovo-yoga-7-83dj00.webp",
        "productName": "Lenovo Yoga 7 83DJ007UIN Laptop (Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,01,990",
        "rating": "4.7",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "Integrated Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BsAHj-SrCPJBCAnhrhArnrysuhyihDRPKooll7Rlh-hrhhaFhrhrhhacBrWahrhrBi5otYD2QuIhrFB5TyprmaAWmN.U"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icqU6ly66-w280-h280/msi-katana-17-b13vgk.webp",
        "productName": "MSI Katana 17 B13VGK-1231IN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,32,990",
        "rating": "4",
        "specScore": "73",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "17.3 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB-r~.rQwko--BlJhrhArnrysuhyihDRPw_K_dVwdh-hrhhaFhrhrhhacBrWahrhrBi5rnFyOXiGhrFB5Q5RrTnQVnV38"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXYmi3ng-w280-h280/msi-thin-15-b13uc-18.webp",
        "productName": "MSI Thin 15 B13UC-1805IN Gaming Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB  RTX 3050 Graph)",
        "price": "₹63,990",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqv8Z1JUA_x.rU4hrhArnrysuhyihDRPw0l-5~eph-hrhhaFhrhrhhacBrWahrhrBi5lutWUTuthrFB5JXTqe4esNHb3"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilZ9Zk1qn-w280-h280/msi-thin-15-b13ve-18.webp",
        "productName": "MSI Thin 15 B13VE-1802IN Gaming Laptop (13th Gen Core i5/ 16GB/ 1T SSD/ Win11 Home/ 6GB RTX4050 Graph)",
        "price": "₹79,990",
        "rating": "4.4",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI_5baB~z1VRleihrhArnrysuhyihDRPw0lvloz~h-hrhhaFhrhrhhacBrWahrhrBi5ZU2s5rnihrFB5E7OuFqszvZGl"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXYmi3ng-w280-h280/msi-thin-15-b13uc-18.webp",
        "productName": "MSI Thin 15 B13UC-1804IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB RTX3050 Graph)",
        "price": "₹72,990",
        "rating": "4.1",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq_dR~ks3s3gFjjhrhArnrysuhyihDRPw0lmxSf7h-hrhhaFhrhrhhacBrWahrhrBi5B555PGsBhrFB5BO_VQ57VJpPf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSXYmi3ng-w280-h280/msi-thin-15-b13ucx-1.webp",
        "productName": "MSI Thin 15 B13UCX-1806IN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹67,990",
        "rating": "4.65",
        "specScore": "63",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqzO~OEwti~Pr2lhrhArnrysuhyihDRPw0ldp5Zfh-hrhhaFhrhrhhacBrWahrhrBi5nFatAyDAhrFB5AeJTstVZXa8Z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6uEQQsGY-w280-h280/msi-cyborg-15-a12udx.webp",
        "productName": "MSI Cyborg 15 A12UDX-1048IN Gaming Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB RTX3050 Graph)",
        "price": "₹78,990",
        "rating": "4.5",
        "specScore": "71",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqr4O~BnEEP_bodhrhArnrysuhyihDRPw0~S1dooh-hrhhaFhrhrhhacBrWahrhrBi5HIQHBFtHhrFB5biCjkkZ2dqd8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZitQrlIj-w280-h280/dell-inspiron-5330-2.webp",
        "productName": "Dell Inspiron 5330 2024 Laptop (Intel Core Ultra 5 125H/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹87,990",
        "rating": "4.65",
        "specScore": "56",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5x RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "13.3 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK4U7tND0SU1qlZjhrhAA3snrh7iaTTcYuFBY3suc4ZZPcYuUaTcAs3acCTU3rc4c5HUtcWaucusUa6ssOcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55c5ZcZcYuAtcNticBTCFciYFBTrIcnFcsggYAacoPo5cBTrUYuCncFYThCc5coHcOWch-hDZP4X4XhrhhaFhrhrhhacBrWahrhrBi5bUANgsgPhrFB5qV~HRBZzfClX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZitQrlIj-w280-h280/dell-inspiron-5330-l.webp",
        "productName": "Dell Inspiron 5330 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹96,099",
        "rating": "4.3",
        "specScore": "59",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "13.3 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK4Ik0GVkip2r_nehrhAA3snrh7iaTTcYuFBY3suc4ZZPcYuUaTcAs3acCTU3rcGc5HUtcWaucusUa6ssOcTrBUsBc5bW6c5U6cFFic8Yuis8Fc55c5ZcZcYuAtcNticBTCFciYFBTrIcnFcsggYAacoPo5cBTrUYuCncFYThCc5coHcOWch-hDZP4XbHhrhhaFhrhrhhacBrWahrhrBi5nUgXtW5AhrFB5nx_8qUfUBu3T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLvt0fyu2-w280-h280/dell-14-vostro-3420.webp",
        "productName": "Dell 14 Vostro 3420 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹45,289",
        "rating": "4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw6ZfsHRCwUfEgZhrhArnrysuhyihDRPKl-pzwK-h-hrhhaFhrhrhhacBrWahrhrBi55CQAsrHHhrFB5lD0NgzOQ7mr1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIhe53CkR-w280-h280/dell-inspiron-3530-o.webp",
        "productName": "Dell Inspiron 3530 OIN353034011RINB1M Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹51,790",
        "rating": "4.5",
        "specScore": "47",
        "features": [
            "13th Gen Intel Core i5 1334U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYw2-GrS~U1g6S6hrhAgTYBOr3Uh7iaTTcYuUaTcAs3acY4c5ZUtcWauc5ZZHCcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacYuFBY3sucZ4ZPcUtYucTYWtUcTrBUshDhDh85rHAX6Xi66biGhmBYihkwkpSf7R.eJje~VlRhrhhaFhrhrhhacBrWahrhrBi5inYo2QYihrFB5qp6KQR89k_t2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-idpETxb6X-w280-h280/hp-omen-16-xf0100ax.webp",
        "productName": "HP Omen 16-xf0100AX Gaming Laptop (AMD Ryzen 9 7940HS/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,61,990",
        "rating": "4.4",
        "specScore": "77",
        "features": [
            "7th Gen AMD Ryzen 9 7940HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Xs0df_2fa6EufGhrhArnrysuhyihDRPK5Rzle_xh-hrhhaFhrhrhhacBrWahrhrBi5ZFi3tNnYhrFB5rCDlmk-y7ypk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaaFCkfGh-w280-h280/asus-rog-zephyrus-g1.webp",
        "productName": "Asus ROG Zephyrus G16 GU605MI-QP253WS Gaming Laptop ( Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹2,19,990",
        "rating": "4.5",
        "specScore": "77",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9Nbg9rtDkgir_E.bhrhArnrysuhyihDRPKo4Jllp5h-hrhhaFhrhrhhacBrWahrhrBi5WCDbIOInhrFB5Vdb687_D.umd"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ix1L7LnHo-w280-h280/asus-rog-strix-g16-2.webp",
        "productName": "Asus ROG Strix G16 2023 G614JIR-N4062WS Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,99,990",
        "rating": "4.75",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NPE1HBBAa5OWt9dhrhArnrysuhyihDRPKo404peph-hrhhaFhrhrhhacBrWahrhrBi5uYnTD8G8hrFB5ax9lBrKRFD13"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUKUwXNFX-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "Acer Swift Go 14 SFG14-73 NX.KSGSI.002 Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹94,990",
        "rating": "4.15",
        "specScore": "64",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Arc Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY6CuyaUwfmYSzdhrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcsTaicYuUaTcAs3acCTU3rcGc544tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacFgW5HcGZcG56IcUtYucTYWtUcTrBUshDhDh85GAlHioZAoZPAhmBYihkwkp7.SoEHj.074-zhrhhaFhrhrhhacBrWahrhrBi5XD5rg6BFhrFB5lKwVR1bqxa-A"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqF3kQXUY-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 Gaming Laptop (AMD Ryzen 5 7535HS/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹62,990",
        "rating": "4.1",
        "specScore": "66",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwTYC4jGvi9jAbUhrhArnrysuhyihDRPK57wvw_zh-hrhhaFhrhrhhacBrWahrhrBi52guUPBUshrFB5EmPNd49EPWt8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i166LZbQV-w280-h280/lenovo-loq-83dv00hbi.webp",
        "productName": "Lenovo LOQ 83DV00HBIN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,03,990",
        "rating": "4.45",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJeT_FC0ve~d5z-0hrhArnrysuhyihDRPw_X1SVo1h-hrhhaFhrhrhhacBrWahrhrBi5PA2XAX6XhrFB5ESdBy~JOUjUK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGul9JzaI-w280-h280/hp-15-fd1095tu-lapto.webp",
        "productName": "HP 15-fd1095TU Laptop (Intel Core 3 100U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹44,569",
        "rating": "4.15",
        "specScore": "50",
        "features": [
            "Intel Core 3 Processor Series 1 100U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq7egsfETJqQVXShrhArnrysuhyihDRPKobHopRxh-hrhhaFhrhrhhacBrWahrhrBi5rBH5oonNhrFB5Ro-x942vezPB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLSZ424xk-w280-h280/hp-15-fd1097tu-lapto.webp",
        "productName": "HP 15-fd1097TU Laptop (Intel Core 5 120U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹67,140",
        "rating": "4.2",
        "specScore": "53",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqze--Ygi~oWSfyhrhArnrysuhyihDRPKob5~JlZh-hrhhaFhrhrhhacBrWahrhrBi55GFF3NG2hrFB5-9GmaedeP3QV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGul9JzaI-w280-h280/hp-15-fd1095tu-lapto.webp",
        "productName": "HP 15-fd1095TU Laptop (Intel Core 3 100U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹44,569",
        "rating": "4.15",
        "specScore": "50",
        "features": [
            "Intel Core 3 Processor Series 1 100U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq7egsfETJqQVXShrhArnrysuhyihDRPKobHopRxh-hrhhaFhrhrhhacBrWahrhrBi5rBH5oonNhrFB5Ro-x942vezPB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icZpYpz2Q-w280-h280/lenovo-loq-15iax9i-8.webp",
        "productName": "Lenovo LOQ 15IAX9I 83FQ002QIN Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹56,490",
        "rating": "4.6",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Intel Integrated ARC A530M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwtzxiep9ozbv~lhrhArnrysuhyihDRPK5_7._flh-hrhhaFhrhrhhacBrWahrhrBi5B2DIQiGZhrFB5iru~pzoWyBWz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDVfAVVp0-w280-h280/msi-thin-15-b12uc-16.webp",
        "productName": "MSI Thin 15 B12UC-1690IN Gaming Laptop (12th Gen Core i7/ 16GB/ 1TB  SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹69,990",
        "rating": "4.65",
        "specScore": "65",
        "features": [
            "12th Gen Intel Core i7 12650H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqEaA1D3xR0qeqjhrhArnrysuhyihDRPw0l0zRVKh-hrhhaFhrhrhhacBrWahrhrBi58DWUUTglhrFB5o6ePDXBay.~~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igGrLyLjM-w280-h280/asus-tuf-gaming-f15.webp",
        "productName": "Asus TUF Gaming F15 FX506HF-HN077WS Gaming Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹51,985",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "11th Gen Intel Core i5 11260H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIS6u8ed3wZOVRqhrhArnrysuhyihDRPKoS.5_~Jh-hrhhaFhrhrhhacBrWahrhrBi5nnQlX6NnhrFB5HwPjqvtPVmdz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iB2untrsA-w280-h280/lenovo-loq-15iax9-83.webp",
        "productName": "Lenovo LOQ 15IAX9 83GS009RIN Gaming Laptop (12th Gen Core i5/ 12GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,490",
        "rating": "4.4",
        "specScore": "62",
        "features": [
            "12th Gen Intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "12 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzFgUYOzdsUOqPWhrhAgTYBOr3Uh7Taus2scTsNcoPoHcYuUaTcAs3acY4c5oUtcWauc5oH4PtDc5ocW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54YrDli5cWrnhNcTrBUshDhDh8Hr5lGZPi5X56HhmBYihkwkpSfl.XbRzezlj7hrhhaFhrhrhhacBrWahrhrBi5CDri6iFAhrFB5VJwRwCyZbm3S"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioJ7u0PSA-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 ‎PHN16-72 NH.QNPSI.003 Gaming Laptop (14th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,29,999",
        "rating": "4.5",
        "specScore": "74",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ808arxyaJ6sTSuEFPqhrhAA3snrh7rAa3cBhBrUs3ctaTYsFcuasc5bcYuUaTcAs3acYGc5HUtcWaucWrnhNcTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnacbW6cW3rBtYAFc5bcYuAtc5b4ctyc8CDWrcYBFciYFBTrIcu2YiYrcWags3Aac3UDcHP4Pcr6IFFrTchncocXcOWch-hDZP4XXXhrhhaFhrhrhhacBrWahrhrBi5bACD6bAPhrFB5mGU2RD7swY-P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGWlh0vI3-w280-h280/lenovo-legion-5-83dg.webp",
        "productName": "Lenovo Legion 5 83DG009DIN Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,67,990",
        "rating": "4.6",
        "specScore": "77",
        "features": [
            "14th Gen Intel Core i7 14650HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv9JIRR_xaVoNkkUHjRhrhAgTYBOr3Uh7Taus2scTaWh3c4coPoHcYuUaTcAs3acYGc5HUtcWauc5Hb4PtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPGPc5bY3DlcWrnhNcTrBUshDhDh8oX4GoigrlZriPhmBYihkwkp7fex7e70w1.V7hrhhaFhrhrhhacBrWahrhrBi5OyWHutWPhrFB5aVfmG~l-B59B"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTA0jPnfv-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 NH.QPESI.001 Gaming Laptop (AMD Ryzen 7 7735HS/ 16GB/ 512GB SSD/ Win11/ 6GB RTX 4050 Graph)",
        "price": "₹82,990",
        "rating": "4",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 7 7735HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY0Gkz.EX2Yr5NihrhAgTYBOr3Uh7rAa3cuYU3scrnic3IyaucGcsAUrcAs3acGGZ4tFc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacbcW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pcru254cH5cWrnhNcTrBUshDhDh8A6gaHXbGiPArGhmBYihkwkp7.dG.Gx.xjq.xhrhhaFhrhrhhacBrWahrhrBi56a8tutBAhrFB5D5AzoVD9CeSD"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMXfbEDo8-w280-h280/asus-zenbook-duo-ole.webp",
        "productName": "Asus Zenbook Duo OLED 2024 UX8406MA-QL761WS Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,19,990",
        "rating": "4",
        "specScore": "70",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~JeQ1DXbF2mCExqhrhAgTYBOr3Uh7rFCFcyau6ssOciCscsTaicYuUaTcAs3acCTU3rcGc544tcZocW6c5cU6cFFic8Yuis8Fc55ctsnacCDXHPbnrcNTGb58FciCrTcFA3aaucTrBUshDhDh85HZaZ64ZHPZoihmBYihkwkp7fex7d~Zfzfd~hrhhaFhrhrhhacBrWahrhrBi5848Z8a3XhrFB58wupSvqqjfO1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7lBALSIt-w280-h280/msi-creator-16-ai-st.webp",
        "productName": "MSI Creator 16 AI Studio  A1VHG-058IN Creator Laptop (Intel Core Ultra 9 185H/ 64GB/ 2TB SSD/ Win11/ 12GB Graph)",
        "price": "₹3,09,990",
        "rating": "4.7",
        "specScore": "93",
        "features": [
            "1st Gen Intel Core Ultra 9 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "64 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "16 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGIHaZo8..0qdU_3hrhAgTYBOr3Uh7nFYcA3arUs3c5bcrYcFUCiYscYuUaTcAs3acCTU3rclc5FUcWauc5X4tcbHcW6cocU6cFFic8Yuis8Fc55ctsnac5ocW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPXPcr52tWcP4XYucTrBUshDhDh8ol6bH5ZPabPoihmBYihkwkp7.JZGv1bz~77phrhhaFhrhrhhacBrWahrhrBi5FZYYobYZhrFB5dBQly0d6q6fv"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixtZDP5CT-w280-h280/msi-pulse-17-ai-c1vg.webp",
        "productName": "MSI Pulse 17 AI C1VGKG-030IN Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11/ 8GB RTX4070 Graph)",
        "price": "₹1,85,990",
        "rating": "4.65",
        "specScore": "82",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "17 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_RgqHFTZ1390l__hrhArnrysuhyihDRPw_xoe-ooh-hrhhaFhrhrhhacBrWahrhrBi5IPyBWW5DhrFB5jz9SgTPRNaZm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWCA4Hlvc-w280-h280/msi-pulse-16-ai-c1vg.webp",
        "productName": "MSI Pulse 16 AI C1VGKG-028IN Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,80,990",
        "rating": "4",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB1._injTEpTij_bhrhArnrysuhyihDRPw0mbzwmdh-hrhhaFhrhrhhacBrWahrhrBi5blA2ui5ohrFB5ZDp.fpPuTkvw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWCA4Hlvc-w280-h280/msi-pulse-16-ai-c1vg.webp",
        "productName": "MSI Pulse 16 AI C1VGKG-029IN Gaming Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,64,990",
        "rating": "4.6",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBdz8QwWzVSrTj8VhrhArnrysuhyihDRPw_K_0K7.h-hrhhaFhrhrhhacBrWahrhrBi56Wyg6iDrhrFB5nxGrn4iBpJrG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQwIEfS0z-w280-h280/msi-sword-16-hx-b14v.webp",
        "productName": "MSI Sword 16 HX B14VGKG-207IN Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 8GB RTX4070)",
        "price": "₹1,50,990",
        "rating": "4.25",
        "specScore": "79",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_GEoxQnz4W8TjmyhrhArnrysuhyihDRPw_KS_ee.h-hrhhaFhrhrhhacBrWahrhrBi5OWa5BiByhrFB57Sv-JRjUBkx1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQwIEfS0z-w280-h280/msi-sword-16-hx-b14v.webp",
        "productName": "MSI Sword 16 HX B14VEKG-210IN Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home/ 6GB RTX4050)",
        "price": "₹1,21,990",
        "rating": "4.65",
        "specScore": "77",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_ZFRTaN0_pQA4g8hrhArnrysuhyihDRPw_KKJzGKh-hrhhaFhrhrhhacBrWahrhrBi5It45uFtFhrFB5pRiWr41AZjQo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWCA4Hlvc-w280-h280/msi-pulse-16-ai-c1vf.webp",
        "productName": "MSI Pulse 16 AI C1VFKG-030IN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,45,990",
        "rating": "4.55",
        "specScore": "77",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBmbWlbj3nSmr_8shrhArnrysuhyihDRPw_Kd0J-Jh-hrhhaFhrhrhhacBrWahrhrBi5F5NPQNlAhrFB5IP0Seoz7xX.s"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iBfnhDdhJ-w280-h280/hp-omen-16-wf0061tx.webp",
        "productName": "HP Omen 16-wf0061TX Gaming Laptop (13th Gen Core i9/ 32GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,89,990",
        "rating": "4.6",
        "specScore": "80",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16.1 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHP%2520Omen%252016-wf0061TX%2520Gaming%2520Laptop%2520(13th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqEojy34E-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios Neo 16 2024 ‎PHN16-72 Gaming Laptop (14th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,29,990",
        "rating": "4.15",
        "specScore": "75",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Hi-f1.mq0XDjUthrhArnrysuhyihDRPw.v05eeKh-hrhhaFhrhrhhacBrWahrhrBi5Tu3DOiIWhrFB5ux9xfbS0tkRq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFs6KHBME-w280-h280/acer-nitro-v-anv15-4.webp",
        "productName": "Acer Nitro V ANV15-41 Gaming Laptop (AMD Ryzen 5 7535HS/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹59,990",
        "rating": "4.65",
        "specScore": "64",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwQPmHQlsIl-kqWhrhArnrysuhyihDRPK57w4Rbeh-hrhhaFhrhrhhacBrWahrhrBi5T6ZQZFgChrFB5faeevPXUsVN_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imZeeixsX-w280-h280/acer-aspire-5-a515-5.webp",
        "productName": "Acer Aspire 5 A515-58M UN.KHFSI.004 Gaming Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹39,990",
        "rating": "4.65",
        "specScore": "51",
        "features": [
            "13th Gen Intel Core i3 1305U",
            "5 Cores (1P + 4E), 6 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYHB8HtJvyS7JpthrhAgTYBOr3Uh7rAa3crFBY3ac4c54cYuUaTcAs3acYZc5ZUtcWauc5ZP4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacr454c4XncUtYucTYWtUcTrBUshDhDh84gbgGbiilbrGbhmBYihkwkp7_pf4oqq_w-pdhrhhaFhrhrhhacBrWahrhrBi5XGBrZbbahrFB5akFa5TZHPIWq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5l2W3dtO-w280-h280/hp-250-g9-8y2y9pa-la.webp",
        "productName": "HP 250 G9 8Y2Y9PA Laptop (Intel Celeron N4500/ 8 GB RAM/ 256GB SSD/ DOS)",
        "price": "₹23,990",
        "rating": "4.15",
        "specScore": "43",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1366 x 768 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzfezb_.2ffQJY~hrhAgTYBOr3Uh7tBco4PcWlcYuUaTcAaTa3suciCrTcAs3ac5oUtcWaucH4PPCcXcW6co4bcW6cFFic8Yuis8Fc55cB3scXIoIlBrcTrBUshDhDh84G4Hioa4PoGA4hmBYihkwkp7Jw7.VffXbVdXhrhhaFhrhrhhacBrWahrhrBi5545tY54NhrFB5ETufD6meuVFt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikHXHHUMd-w280-h280/hp-chromebook-11mk-g.webp",
        "productName": "HP Chromebook 11MK G9 EE Touch Laptop (MediaTek MT8183/ 4GB/ 32GB eMMC/ Chrome OS)",
        "price": "₹21,990",
        "rating": "4.35",
        "specScore": "33",
        "features": [
            "MediaTek Kompanio 500 500",
            "Octa Core",
            "4 GB LPDDR4X RAM",
            "32 GB Hard Disk",
            "Arm Mali-G72 MP3",
            "11.6 inches, 1366 x 768 pixels, Touch Screen",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFt2-DfRlTYkzTW3hrhAgTYBOr3Uh7tBcUsCAtcAt3sna6ssOcoPoHcnaiYrUaOcnUX5XZcHcW6cZocW6cannAcFUs3rWacAt3snacsFc55nOcWlh-hDh844lbaGPHX5AXXhmBYihkwkp7.xx_~l7q_10vhrhhaFhrhrhhacBrWahrhrBi5846CgDZUhrFB5HHnX6mvsZ20g"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXObWCRDP-w280-h280/lenovo-thinkbook-15.webp",
        "productName": "Lenovo ThinkBook 15 G5 21JFA02RIN Laptop (AMD Ryzen 3 7330U/ 8GB/ 512 GB SSD/ Win11)",
        "price": "₹34,490",
        "rating": "4",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 3 7330U",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon AMD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqj_gTklAzwNgedhrhArnrysuhyihDRPw.GR-bffh-hrhhaFhrhrhhacBrWahrhrBi55g8alTAlhrFB5e_-jI1NPs5nZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqOrk6zsh-w280-h280/lenovo-legion-pro-5.webp",
        "productName": "Lenovo Legion Pro 5 83DF003PIN Gaming Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,98,490",
        "rating": "4.65",
        "specScore": "86",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9NPpxdsUnnH5nTk8hrhArnrysuhyihDRPw_1f4Sxoh-hrhhaFhrhrhhacBrWahrhrBi5TBlHui2QhrFB5m~flXOaTAWy0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6K5S9MUs-w280-h280/hp-15s-fq5331tu-lapt.webp",
        "productName": "HP 15s-fq5331TU Laptop (12th Gen Core i5/ 8GB/ 1TB SSD/ Win11 Home)",
        "price": "₹50,490",
        "rating": "4.3",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "1 TB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqV0OGam.JXqsmOhrhArnrysuhyihDRPK5HblxJ4h-hrhhaFhrhrhhacBrWahrhrBi5P4aUtUHthrFB5fDWskf~APWsH"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6tB6Xc2s-w280-h280/hp-15s-fq5328tu-lapt.webp",
        "productName": "HP 15s-fq5328TU Laptop (12th Gen Core i3/ 8GB/ 1TB SSD/ Win11 Home)",
        "price": "₹39,990",
        "rating": "4.2",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrztHxDr9HSp9ndqhrhAgTYBOr3Uh7tBcgNcFa3YaFcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c5cU6cFFic8Yuis8Fc55ctsnac54FcgN4ZoXUCcUtYucTYWtUcTrBUshDhDh8aGbagPoiAAr5ghmBYihkwkpSoxfv-H.SKjwZhrhhaFhrhrhhacBrWahrhrBi58HZiiuIHhrFB5TQ_GTnSxoP.d"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ie8oZMA6u-w280-h280/microsoft-surface-la.webp",
        "productName": "Microsoft Surface Laptop 6 (Intel Core Ultra 7 165H/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,99,990",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "Intel Core Ultra 7 Series 1 165H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB  RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "13.5 inches, 2256 x 1504 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMicrosoft%2520Surface%2520Laptop%25206%2520(Intel%2520Core%2520Ultra%25207%2520165H%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9G3dZHBS-w280-h280/microsoft-surface-pr.webp",
        "productName": "Microsoft Surface Pro10 Laptop (Intel Core Ultra 7 165U/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,99,990",
        "rating": "4.45",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 7 165U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Graphics",
            "13 inches, 2880 x 1920 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMicrosoft%2520Surface%2520Pro10%2520Laptop%2520(Intel%2520Core%2520Ultra%25207%2520165U%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iCX2E1wg4-w280-h280/msi-raider-ge78-hx-1.webp",
        "productName": "MSI Raider GE78 HX 14VIG-804IN Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 16GB Graph)",
        "price": "₹3,39,990",
        "rating": "4.3",
        "specScore": "93",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "17 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBNpY6NjlOUSFCoNhrhArnrysuhyihDRPK5xe7eeKh-hrhhaFhrhrhhacBrWahrhrBi52GCg5NDnhrFB5t1q24sZ.vHfm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAfj0NSRR-w280-h280/msi-crosshair-16-hx.webp",
        "productName": "MSI Crosshair 16 HX D14VGKG-205IN Gaming Laptop (14th Gen Core i7/ 32GB/ 1TB SSD/ Win11 Home/ 8GB RTX4070)",
        "price": "₹1,79,890",
        "rating": "4.5",
        "specScore": "83",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1440 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv76g1k19F~7Jos175IhrhAgTYBOr3Uh7nFYcA3sFFtrY3c5bctDcYuUaTcAs3acYGc5HUtcWauc5HGPPtDcZocW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHPGPci5H2WOWcoP4YucWrnhNcTrBUshDhDh86lX4roX5iAA5lhmBYihkwkp7fe7d~pqER.qwhrhhaFhrhrhhacBrWahrhrBi5oZltrlbQhrFB5UyBF7awi8H~D"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iCcMMgrs2-w280-h280/lenovo-legion-pro-7.webp",
        "productName": "Lenovo Legion Pro 7 83DE001JIN Gaming Laptop (13th Gen Core i9/ 32GB/ 1TB SSD/ Win11 Home/ 16GB Graph)",
        "price": "₹3,35,000",
        "rating": "4.55",
        "specScore": "89",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_6JyQDVCZ.HXpvBhrhArnrysuhyihDRPw_1_RSKSh-hrhhaFhrhrhhacBrWahrhrBi5a6gsyGyWhrFB5xsZ.P20FOTeX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip1JcY0vg-w280-h280/hp-250-g9-6s798ea-la.webp",
        "productName": "HP 250 G9 6S798EA Laptop (Intel Celeron N4500/ 8 GB RAM/ 256GB SSD/ Win 11)",
        "price": "₹22,999",
        "rating": "4",
        "specScore": "46",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFt2njJ-JipxisFKhrhAgTYBOr3Uh7tBco4PcWlcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacUtYucTYWtUcTrBUshDhDh8HZggHAX46G5aihmBYihkwkp7.Vo.oKzo10_.hrhhaFhrhrhhacBrWahrhrBi5NQWOtb6rhrFB5o_D~qAWYOCGI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC7cJQcQ0-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV00HAIN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,03,990",
        "rating": "4.75",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~q6SvxXJo.gQyCHhrhAgTYBOr3Uh7Taus2scTsNcoPoHcYuUaTcAs3acYGc5ZUtcWauc5Zb4PtDc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc54Y3DlcWrnhNcTrBUshDhDh8HrH6ll4Gb5gX6hmBYihkwkp7fex7q1jXJ~7ShrhhaFhrhrhhacBrWahrhrBi526aaDDlZhrFB56Fw1JC.5CEXT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifoQZvlRE-w280-h280/asus-zenbook-duo-ole.webp",
        "productName": "Asus Zenbook Duo OLED 2024 UX8406MA-QL551WS Laptop (Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,79,990",
        "rating": "4.3",
        "specScore": "63",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_jsKHStG7bIu6FvhrhArnrysuhyihDRPw_1J7.Kxh-hrhhaFhrhrhhacBrWahrhrBi5lDNNsAHnhrFB5dsxYTKzVBrV4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNPv63FTj-w280-h280/asus-zenbook-duo-ole.webp",
        "productName": "Asus Zenbook Duo OLED 2024 UX8406MA-QL971WS Laptop (Intel Core Ultra 9 185H/ 32GB/ 2TB SSD/ Win11)",
        "price": "₹2,39,990",
        "rating": "4",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "2 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~f2UKUIsU.SNgoVhrhAgTYBOr3Uh7rFCFcyau6ssOciCscsTaicYuUaTcAs3acCTU3rclc5X4tcZocW6cocU6cFFic8Yuis8Fc55ctsnacCDXHPbnrcNTlG58FciCrTcFA3aaucTrBUshDhDh86HAGXPoGoo65ghmBYihkwkp7fex7fKE.0o_lhrhhaFhrhrhhacBrWahrhrBi5Qroyai6ahrFB57ZvNNr.DuvP9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ih7iDSqoT-w280-h280/razer-blade-18-gamin.webp",
        "productName": "Razer Blade 18 Gaming Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11 Home/ 16GB Graph)",
        "price": "₹3,49,990",
        "rating": "4.15",
        "specScore": "88",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "18 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DRazer%2520Blade%252018%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%252016GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEHkSsxYO-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS0X800 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹71,990",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw3jobooW2uzAK4hrhArnrysuhyihDRPw0~vxz-mh-hrhhaFhrhrhhacBrWahrhrBi5BWAIoYb6hrFB5wVxtaptSSAEW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2sZgT6qN-w280-h280/dell-alienware-m16-r.webp",
        "productName": "Dell Alienware M16 R2 2024 Gaming Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win 11/ 8GB Graph)",
        "price": "₹2,14,190",
        "rating": "4.1",
        "specScore": "80",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GEFORCE RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJO4CyQZX87B2unlhrhArnrysuhyihDRPwfm_KHV4h-hrhhaFhrhrhhacBrWahrhrBi5yntFaZ35hrFB5rsbjNP-QOvVa"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixjw4bvlQ-w280-h280/dell-g15-5530-15-6-g.webp",
        "productName": "Dell G15-5530 15.6 Gaming Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹70,540",
        "rating": "4.7",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwNfenp8X5AaksRhrhArnrysuhyihDRPwvV0GJVzh-hrhhaFhrhrhhacBrWahrhrBi5HYXWPyUDhrFB5xyB11Y8otCpT"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4aattUkQ-w280-h280/asus-zenbook-duo-ole.webp",
        "productName": "Asus Zenbook Duo OLED 2024 UX8406MA-QL961WS Laptop (Intel Core Ultra 9 185H/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹2,39,990",
        "rating": "4.45",
        "specScore": "73",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_m2~wZJ--PWJOQphrhArnrysuhyihDRPw_1_mpRSh-hrhhaFhrhrhhacBrWahrhrBi5ZaByCtDGhrFB5ZxHuv-BIKyJS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imH2zFFem-w280-h280/infinix-inbook-x1-sl.webp",
        "productName": "Infinix INBook X1 Slim Series Laptop (10th Gen Core i7/ 8GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹43,990",
        "rating": "4.3",
        "specScore": "44",
        "features": [
            "10th Gen Intel Core i7 1065G7",
            "Quad Core, 8 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYXPrCF-m1.JT2-hrhAgTYBOr3Uh7YugYuYDcYuUaTcAs3acYGc5PUtcWauc5Pb4WGcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac5oXcn6cW3rBtYAFcDTo5cUtYucTYWtUcTrBUshDhDh8loAXaZaXo5XrPhmBYihkwkp7~S0p-7~fSzE~hrhhaFhrhrhhacBrWahrhrBi536FaBX2ihrFB51Zk~e5ZvA~bB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icVxAgcdI-w280-h280/acer-swift-go-14-202.webp",
        "productName": "Acer Swift Go 14 2024 SFG14-73T Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹89,990",
        "rating": "4.7",
        "specScore": "57",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated ARC Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOqZbsdK8z2i0g2hrhAgTYBOr3Uh7rAa3cF8YgUcWsc5HcUsCAtFA3aaucYuUaTcAs3acCTU3rcGc544tc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacFgW5HcGZUcUtYucTYWtUcTrBUshDhDh8ZlZag6lHGiXArhmBYihkwkp7.SoExVqR411HhrhhaFhrhrhhacBrWahrhrBi5gNCgZOXNhrFB5EnuqBt3WdjSY"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaxcihevC-w280-h280/acer-predator-helios.webp",
        "productName": "Acer Predator Helios 16 ‎PH16-72 NH.QNXSI.003 Gaming Laptop (14th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB  RTX4070)",
        "price": "₹1,99,990",
        "rating": "4.05",
        "specScore": "80",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_KSpFq_B7O5_ZN~hrhArnrysuhyihDRPw_1_zH_Kh-hrhhaFhrhrhhacBrWahrhrBi5gulosnOXhrFB5aBmBPwqfvCk8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy7HL4853-w280-h280/dell-alienware-m16-r.webp",
        "productName": "Dell Alienware M16 R2 2024 Gaming Laptop (Intel Core Ultra 7 155H / 16GB/ 1TB SSD/ Win 11/ 6GB Graph)",
        "price": "₹1,51,919",
        "rating": "4",
        "specScore": "70",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GEFORCE RTX 4050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJfO1lD~7pQg2xTdhrhArnrysuhyihDRPKRmxe4l4h-hrhhaFhrhrhhacBrWahrhrBi5CNgtYQTChrFB5-0pS8RQWsHF_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isEFWPUh7-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS0LT00 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹47,899",
        "rating": "4.35",
        "specScore": "51",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzn5xSU3tlVSGJfhrhAgTYBOr3Uh7Taus2scYuUaTcAs3acYZc5ZUtcWaucXcW6c45ocW6cFFicisFcUtYuOBrica5Hc4c6CFYuaFFcTrBUshDhDh8Z6gro65igGXAZhmBYihkwkpSoEERoeKe_jHqhrhhaFhrhrhhacBrWahrhrBi5yZy4IY8GhrFB5dVR5YgvBvCmE"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC6mdOERB-w280-h280/lenovo-ideapad-pro-5.webp",
        "productName": "Lenovo IdeaPad Pro 5 83D4002NIN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,24,990",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 2048 x 1280 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_Hl3vR3s2SuCQHWhrhArnrysuhyihDRPwzVHoKedh-hrhhaFhrhrhhacBrWahrhrBi55UXs5oPGhrFB51iPN2fdBVvg."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-io68BdQRA-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus VivoBook 15 X1500EA-EJ122WS Laptop (Intel Pentium Gold 7505/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹27,990",
        "rating": "4.2",
        "specScore": "50",
        "features": [
            "Intel Pentium Gold 7505",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqbR_pZwiVmlKDRhrhArnrysuhyihDRPw.ZVHoK_h-hrhhaFhrhrhhacBrWahrhrBi5WygyoO8ZhrFB5n8Sg6Xx~.lq0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAP9KPw2o-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-41 Laptop (AMD Ryzen 7 5700U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹42,990",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "5th Gen AMD Ryzen 7 5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQu-f.T~ITvYxWzhrhAgTYBOr3Uh7rAa3crFBY3acThscrnic3IyaucGcsAUrcAs3ac4GPPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacrT54cH5cUtYucTYWtUcTrBUshDhDh8rGAogr455Z6a6hmBYihkwkpSfGH-_J0J0Vx0hrhhaFhrhrhhacBrWahrhrBi5y5POOYbXhrFB58ngnePCxQHD-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilbMq9Zic-w280-h280/honor-magicbook-x16.webp",
        "productName": "Honor MagicBook X16 Pro 2024 BRN-G58 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹49,877",
        "rating": "4.55",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwiHYjDiyge69XmhrhArnrysuhyihDRPw_m0Vd0Rh-hrhhaFhrhrhhacBrWahrhrBi53GuoAFUThrFB5QHBVR6aylZpP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPUpfMc4f-w280-h280/honor-magicbook-x14.webp",
        "productName": "Honor MagicBook X14 Pro 2024 FRI-G58 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹58,972",
        "rating": "4.6",
        "specScore": "52",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB LPDDRx4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwY_8K7f9_2U077hrhArnrysuhyihDRPw_mv1H0-h-hrhhaFhrhrhhacBrWahrhrBi5sU2XgXDThrFB5YKf.qpvrDdzX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQ5FPWWcu-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 ‎15IAH8 83ER00BCIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹54,390",
        "rating": "4.4",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpSDzkrYbF6V4QhrhArnrysuhyihDRPwJ05JzfVh-hrhhaFhrhrhhacBrWahrhrBi5i3AnAlTIhrFB5pqNEaDAWNPly"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip8hc7Q2l-w280-h280/hp-envy-x360-14-fa00.webp",
        "productName": "HP Envy x360 14-fa0038AU Laptop (AMD Ryzen 5 8640HS/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹83,990",
        "rating": "4.4",
        "specScore": "68",
        "features": [
            "8th Gen AMD Ryzen 5 8640HS",
            "Hexa Core, 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2G_KkPilb2lrdSnhrhAA3snrh7tBcau2IcDZbPc5HcgrPPZXrCcrnic3Iyauc4cUsCAtFA3aaucocYuc5cTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtc8CDWrcYBFciYFBTrIcnaUas3cFYThCcrTCnYuCnc5cZlOWch-hDZPGblGhrhhaFhrhrhhacBrWahrhrBi5gW8FX6OyhrFB5eIARUjEgCTQz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivqRFjtc2-w280-h280/lenovo-v14-82ts005di.webp",
        "productName": "Lenovo V14 82TS005DIH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹43,490",
        "rating": "4.35",
        "specScore": "47",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwrKOSiGDiupHyChrhArnrysuhyihDRPwJdmodemh-hrhhaFhrhrhhacBrWahrhrBi5utiDnCubhrFB5Tw7OG491TjB5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ixakMb2NM-w280-h280/lenovo-v14-82tsa0cwi.webp",
        "productName": "Lenovo V14 82TSA0CWIH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹55,490",
        "rating": "4.5",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwt5luY_57~EWCihrhArnrysuhyihDRPwJv1415ph-hrhhaFhrhrhhacBrWahrhrBi53DBZ2OGnhrFB5QvWo.W73NFp8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3VCQc7g8-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS13K00 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹86,990",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics comes",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwy-QGV2fFfvGpdhrhArnrysuhyihDRPwJvzzZd_h-hrhhaFhrhrhhacBrWahrhrBi568ZNBNaPhrFB57t~3I_sJbk8C"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imYdFLNRz-w280-h280/hp-envy-x360-15-fe00.webp",
        "productName": "HP Envy x360 15-fe0014TX Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 4GB Graphics)",
        "price": "₹1,37,990",
        "rating": "4.15",
        "specScore": "69",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG0z_B8EwJs6fuN4hrhAgTYBOr3Uh7tBcau2IcDZbPcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFc54cgaPP5HUDcTrBUshDhDh8Gr6ol4gg6ogl6hmBYihkwkp7~zxw0q01-owVhrhhaFhrhrhhacBrWahrhrBi5CDlQIAT8hrFB5PauG_eetsri~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ib1wBlyWe-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2024 X1504VAP-NJ322WS Laptop (Intel Core 3 Processor 100U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹45,990",
        "rating": "4.75",
        "specScore": "53",
        "features": [
            "Intel Core 3 Processor 100U",
            "Hexa Core (2P + 4E), 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw69QUjbKsVjp~5hrhArnrysuhyihDRPw_1_-z41h-hrhhaFhrhrhhacBrWahrhrBi5a36tQ2rlhrFB5PwniJxVDS_S9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irGKrUjBv-w280-h280/asus-vivobook-15-202.webp",
        "productName": "Asus Vivobook 15 2024 X1504VAP-NJ542WS Laptop (Intel Core 5 Processor 120U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹59,990",
        "rating": "4.55",
        "specScore": "55",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwQPmHQlsIl-kqWhrhArnrysuhyihDRPw_1_b~e1h-hrhhaFhrhrhhacBrWahrhrBi5YtrBXNWNhrFB5IDsU6O9Isu5X"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwTc3iDoV-w280-h280/hp-envy-x360-14-fa00.webp",
        "productName": "HP Envy x360 14-fa0052AU Laptop (AMD Ryzen 7 8840HS/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹93,990",
        "rating": "4.35",
        "specScore": "69",
        "features": [
            "8th Gen AMD Ryzen 7 8840HS",
            "Octa Core, 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqQ6YDpljOPGER4hrhArnrysuhyihDRPwJxxfpXvh-hrhhaFhrhrhhacBrWahrhrBi568XnGlZThrFB55XvgCUd5FVi_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKloyH0hn-w280-h280/hp-envy-x360-14-fc01.webp",
        "productName": "HP Envy x360 ‎14-fc0100TU Laptop (Intel Core Ultra 7 155U/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,29,990",
        "rating": "4.1",
        "specScore": "73",
        "features": [
            "Intel Core Ultra 7 155U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "Integrated Intel Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv9JIbvP4v9BOdC_sRlhrhAgTYBOr3Uh7tBcau2IcYuUaTcAs3acCTU3rcGc544CcZocW6c5cU6cFFic8Yuis8Fc55ctsnac5HcgAP5PPUCcUtYucTYWtUcTrBUshDhDh86b6gHil6HZ6oohmBYihkwkp7fxpKRR~.SH-KhrhhaFhrhrhhacBrWahrhrBi5PtCaYFQGhrFB51tA29Avz~dwP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4soLSL8j-w280-h280/lenovo-legion-pro-7i.webp",
        "productName": "Lenovo Legion Pro 7i 2024 Gaming Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹2,97,758",
        "rating": "4",
        "specScore": "89",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "12 GB NVIDIA Geforce RTX 4080",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DLenovo%2520Legion%2520Pro%25207i%25202024%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%2520Home%252F%252012GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iW0EZC1TP-w280-h280/lenovo-thinkpad-p14s.webp",
        "productName": "Lenovo ThinkPad P14s 21HF001FIG Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Pro/ 4GB Graphics)",
        "price": "₹1,30,538",
        "rating": "4.7",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "4 GB NVIDIA RTX A500",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJJl6CETwwCZVvvthrhArnrysuhyihDRPw0~.z0b0h-hrhhaFhrhrhhacBrWahrhrBi5ZByBTl86hrFB58OgZCu5C1C3j"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOu8ad0Bc-w280-h280/asus-zenbook-s13-ole.webp",
        "productName": "Asus Zenbook S13 OLED 2024 UX5304MA-NQ752WS Laptop ( Intel Core Ultra 7 155U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,29,990",
        "rating": "4.05",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 7 155U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Intel Iris Xe Graphics",
            "13.3 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~Sinr75NBZOSvEahrhAgTYBOr3Uh7rFCFcyau6ssOcFc5ZcsTaicYuUaTcAs3acCTU3rcGc544Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacCD4ZPHnrcuNG458FcUtYucTYWtUcTrBUshDhDh8a44XbHlr4b6oZhmBYihkwkp7fex7pjVx7ewfhrhhaFhrhrhhacBrWahrhrBi58DHlXICUhrFB5DJ0QHttfne1E"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iRgydQKu2-w280-h280/lenovo-thinkpad-p14s.webp",
        "productName": "Lenovo ThinkPad P14s 21HF001EIG Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Pro)",
        "price": "₹1,08,990",
        "rating": "4.3",
        "specScore": "71",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "4 GB NVIDIA RTX A500",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJzxPPXwDTAs3w-1hrhArnrysuhyihDRPw0~ffm5oh-hrhhaFhrhrhhacBrWahrhrBi5grYtrXlChrFB5QzJ4.Vvjqp5i"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqUt2JIHU-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGK-KS3IN Laptop (Intel Core 7 Processor 150U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹79,999",
        "rating": "4",
        "specScore": "56",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125EdUBvokxAQraSau2ZF8A3HQhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHc54cbcYuAtcAs3acGc5bW6c45oW6cuBG4PDWOcTFZYuh-hrhhaFhrhrhhacBrWahrhrBi5HruunbBXhrFB5blg~HWn1NETQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqbIDBBFz-w280-h280/hp-envy-x360-14-fc01.webp",
        "productName": "HP Envy x360 14-fc0106TU Laptop (Intel Core Ultra 7 155U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,02,999",
        "rating": "4.75",
        "specScore": "68",
        "features": [
            "Intel Core Ultra 7 155U",
            "12 Cores (2P + 8E + 2LP-E), 14 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-dGHmQ8.uDUlCPOBQU5._1J0hrhAA3snrh7tBcau2IcDZbPcYuUaTcAs3acCTU3rcGcUsCAtFA3aaucocYuc5cTrBUsBc5bW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtc8CDWrcYBFciYFBTrIcnFcsggYAacoPo5crUnsFBta3YAc6TCac5cHHcOWch-hDZP4XZXhrhhaFhrhrhhacBrWahrhrBi5urPNB6nlhrFB5HNeJjyWXBZNw"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ioGGCa7zG-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 NP750XGK-KS1IN Laptop (Intel Core 5 Processor 120U/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹63,990",
        "rating": "4.65",
        "specScore": "53",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR4x RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125EdUBvok7V0H7tfx~8r1_fOAhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHc54cbcYuAtcAs3ac4cXW6c45oW6cuBG4PDWOcOF5Yuh-hrhhaFhrhrhhacBrWahrhrBi5CWQ8UolAhrFB5T1n~x5tl0dw8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivpPIbVtr-w280-h280/hp-spectre-x360-14-e.webp",
        "productName": "HP Spectre x360 14-ef2035TU Laptop (13th Gen Core i7/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,53,990",
        "rating": "4.25",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "32 GB LPDDR4X RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "13.5 inches, 3000 x 2000 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmG_.XO0IEWUn~u~3hrhAgTYBOr3Uh7tBcYuUaTcAs3acYGc5ZUtcWauc5Z44CcZocW6c5cU6cFFic8Yuis8Fc55ctsnacagoPZ4UCcUtYucTYWtUcTrBUshDhDh85iiggHZXbiHlXhmBYihkwkp7fjplzS~S71~ShrhhaFhrhrhhacBrWahrhrBi5t4ggilHXhrFB5Q61Q~-3szQs2"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUUPXZPdc-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 83EQ0044IN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹50,490",
        "rating": "4.35",
        "specScore": "57",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqV0OGam.JXqsmOhrhArnrysuhyihDRPwJvewZSeh-hrhhaFhrhrhhacBrWahrhrBi5ZTWZC5TihrFB5D8U5TUp0uSw-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iR52l07by-w280-h280/hp-omen-transcend-14.webp",
        "productName": "HP Omen Transcend 14-fb0007TX Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,50,990",
        "rating": "4.65",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_GEoxQnz4tBDURbhrhArnrysuhyihDRPw_1f5ezVh-hrhhaFhrhrhhacBrWahrhrBi5ZB4WnB63hrFB51E6qFbPdRAAA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ii2lzESi0-w280-h280/lenovo-thinkpad-e16.webp",
        "productName": "Lenovo Thinkpad E16 21JN004GIG Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹63,490",
        "rating": "4.25",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 USB 3.0 Ports"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwnPRINAynURrKVhrhArnrysuhyihDRPw0~K1HZHh-hrhhaFhrhrhhacBrWahrhrBi54C8b4lZAhrFB5tPu..EIV91E5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUFIOAU9g-w280-h280/lenovo-thinkpad-e16.webp",
        "productName": "Lenovo Thinkpad E16 G1 21JN004DIG Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹43,600",
        "rating": "4.75",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 USB 3.0 Ports"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwr7.ECKG1t2-S0hrhArnrysuhyihDRPw0~x4vlVh-hrhhaFhrhrhhacBrWahrhrBi5lAoGis38hrFB5DsSpKQq7yQEq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iYskZ6cXg-w280-h280/hp-envy-x360-15-fe00.webp",
        "productName": "HP Envy x360 15-fe0011TX Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 4GB Graphics)",
        "price": "₹1,25,990",
        "rating": "4",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGEZRESdi6K7ZANdhrhAgTYBOr3Uh7tBcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFc54cgaPP55UDcTrBUshDhDh8brZaAG5AgAlbghmBYihkwkp7fjpl0xRe~eqKhrhhaFhrhrhhacBrWahrhrBi5tIuTn4IihrFB5o.yAxvCP8-ze"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibNWOvV1F-w280-h280/lenovo-ideapad-1-82v.webp",
        "productName": "Lenovo IdeaPad 1 82V700ECIN Laptop (Celeron N4020/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹25,770",
        "rating": "4.4",
        "specScore": "46",
        "features": [
            "4th Gen Intel Celeron N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics 600",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq4wtbG16GSV9xXhrhArnrysuhyihDRPwJveZ_vRh-hrhhaFhrhrhhacBrWahrhrBi5W5bl5bb2hrFB5OFUOr1FCUy4z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-im2bw7Ewh-w280-h280/msi-raider-ge78-hx-1.webp",
        "productName": "MSI Raider GE78 HX 14VHG-805IN Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹2,79,990",
        "rating": "4.45",
        "specScore": "93",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "17 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJFozSzZjVt3PGQIhrhArnrysuhyihDRPwz~SSfp_h-hrhhaFhrhrhhacBrWahrhrBi5QsYAbnDBhrFB5RCPNTugm0oK-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNDCL33xn-w280-h280/msi-cyborg-15-ai-a1v.webp",
        "productName": "MSI Cyborg 15 AI A1VEK-050IN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,03,990",
        "rating": "4.35",
        "specScore": "68",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_5rs1kWPePRKpTyhrhArnrysuhyihDRPw0HolfSeh-hrhhaFhrhrhhacBrWahrhrBi5aa2TA63GhrFB5p_v-qiq4Gtkf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGYMvlqvX-w280-h280/msi-cyborg-15-ai-a1v.webp",
        "productName": "MSI Cyborg 15 AI A1VFK-049IN Gaming Laptop (Intel Core Ultra 7 155H/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,10,990",
        "rating": "4.3",
        "specScore": "69",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB72E-DwSebyNfT7hrhArnrysuhyihDRPw0HZdS~-h-hrhhaFhrhrhhacBrWahrhrBi5G5YAiXsahrFB5yuy1o7VJU1iA"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1UHKr8ox-w280-h280/msi-katana-a15-ai-b8.webp",
        "productName": "MSI Katana A15 AI B8VE-418IN Gaming Laptop (AMD Ryzen 7 8845HS/ 16GB/ 512GB SSD/ Win11 /6GB Graph)",
        "price": "₹94,990",
        "rating": "4.1",
        "specScore": "70",
        "features": [
            "8th Gen AMD Ryzen 7 8845HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.75 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqOZsu4IvJoQqW6hrhArnrysuhyihDRPw04xS.owh-hrhhaFhrhrhhacBrWahrhrBi56OyQ2UtyhrFB5nEl2V9oPROHP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imrHdaMZA-w280-h280/msi-cyborg-15-ai-a1v.webp",
        "productName": "MSI Cyborg 15 AI A1VEK-051IN Gaming Laptop (Intel Core Ultra 5 125H/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹94,990",
        "rating": "4",
        "specScore": "66",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqOZsu4IvJoYFkAhrhArnrysuhyihDRPw0HoGX4Hh-hrhhaFhrhrhhacBrWahrhrBi5O3TyrD8BhrFB5DDnTYUxQZq6r"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iIQiwk80X-w280-h280/msi-stealth-14-ai-st.webp",
        "productName": "MSI Stealth 14 AI Studio A1VGG-054IN Gaming Laptop (Intel Core Ultra 7 155H/ 32GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹2,19,990",
        "rating": "4",
        "specScore": "83",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJOAy3A0o9nZR6pWhrhArnrysuhyihDRPw04wevmoh-hrhhaFhrhrhhacBrWahrhrBi5bZWHrnDHhrFB5jo30SwoFa3KQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iEFytCIeV-w280-h280/apple-macbook-air-20.webp",
        "productName": "Apple MacBook Air 2024 MRYN3HN/A Laptop (Apple M3/ 8GB/ 512GB SSD/ MacOS)",
        "price": "₹1,45,490",
        "rating": "4.15",
        "specScore": "56",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "10-Core GPU",
            "15.3 inches, 2880 x 1864 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_g0CJ9ieIN4Fg3bhrhArnrysuhyihDRPw_oHe..oh-hrhhaFhrhrhhacBrWahrhrBi5N4FBrOiGhrFB50fZVaVz5kVaJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQVPS7tHO-w280-h280/msi-thin-a15-ai-b7uc.webp",
        "productName": "MSI Thin A15 AI B7UC-067IN Gaming Laptop (AMD Ryzen 5 7535H/ 16GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹61,990",
        "rating": "4.3",
        "specScore": "70",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqv53OZxHyjp4FZhrhArnrysuhyihDRPw04xRbK7h-hrhhaFhrhrhhacBrWahrhrBi5gTou86l5hrFB5nPz-Yea38NtN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irC6vnXNc-w280-h280/msi-vector-16-hx-a14.webp",
        "productName": "MSI Vector 16 HX A14VGG-279IN Gaming Laptop (14th Gen Core i7/ 32GB/ 1TB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,95,990",
        "rating": "4.45",
        "specScore": "88",
        "features": [
            "14th Gen Intel Core i7 14700HX",
            "20 Cores (8P + 12E), 28 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJaH_edPN~6eSmz6hrhArnrysuhyihDRPwz~z--bXh-hrhhaFhrhrhhacBrWahrhrBi5yuWTAPPThrFB5WNCp6GSqqQW-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iyhDArKEG-w280-h280/msi-stealth-16-ai-st.webp",
        "productName": "MSI Stealth 16 AI Studio A1VGG-057IN Gaming Laptop (Intel Core Ultra 9/ 32GB/ 2TB SSD/ Win11/ 8GB Graph)",
        "price": "₹2,44,990",
        "rating": "4.55",
        "specScore": "86",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJu3SeVHrP_07EN1hrhArnrysuhyihDRPwz~zx~G5h-hrhhaFhrhrhhacBrWahrhrBi5N5QuQ58WhrFB5AFd8S0aW7aOU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwxd4CQtN-w280-h280/chuwi-herobook-plus.webp",
        "productName": "Chuwi HeroBook Plus Laptop (Intel Celeron N4020/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹18,990",
        "rating": "4.2",
        "specScore": "38",
        "features": [
            "Intel ‎Celeron N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR3 RAM",
            "256 GB SSD",
            "Intel HD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzEBY~ADTpK3Ja9hrhAgTYBOr3Uh7AtC8YcYuUaTcAaTa3suciCrTcAs3ac55UtcWaucuHPoPcXcW6co4bcW6cFFic8Yuis8Fc55ctsnacta3s6ssOcBTCFcTrBUshDhDh8lPPogZiloab5ghmBYihkwkp7fjplVeXZdq1ehrhhaFhrhrhhacBrWahrhrBi5tlW8bIN6hrFB5X4bz9vCg5DS0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iTvkffq3u-w280-h280/hp-victus-15-fa1099t.webp",
        "productName": "HP Victus 15-fa1099TX Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹59,990",
        "rating": "4.25",
        "specScore": "64",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzFNtauub~eXSrahrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc54cgr5PllUDcWrnhNcTrBUshDhDh8ZagbgirAgg5lahmBYihkwkp7fxpKeqVdzdx~hrhhaFhrhrhhacBrWahrhrBi5FtNU88bbhrFB5~pkyJpeQd9SU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaWLzoXY1-w280-h280/msi-modern-15-c13m-0.webp",
        "productName": "MSI Modern 15 C13M-080IN Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹68,990",
        "rating": "4.2",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI~gnIzNWfQgPikhrhArnrysuhyihDRPw0Z.5pZJh-hrhhaFhrhrhhacBrWahrhrBi5BTiIP6oDhrFB5tdjqp~Vw4i9k"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i7d8WGwfD-w280-h280/msi-modern-15-c13m-0.webp",
        "productName": "MSI Modern 15 C13M-079IN Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹78,990",
        "rating": "4.4",
        "specScore": "66",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwCVW8wBrmw_0q.hrhArnrysuhyihDRPw0ZJ~XXRh-hrhhaFhrhrhhacBrWahrhrBi5NUBlHQ3thrFB5ssTUwQ_5s0Qq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imUs60x4u-w280-h280/msi-modern-15-c13m-0.webp",
        "productName": "MSI Modern 15 C13M-081IN Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹58,990",
        "rating": "4.2",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwYfxqyVfwbtiQjhrhArnrysuhyihDRPw0Zf7ZXxh-hrhhaFhrhrhhacBrWahrhrBi55nnU5iCBhrFB5bWNe9ZZnzJrx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5xCyNq9o-w280-h280/chuwi-gemibook-plus.webp",
        "productName": "Chuwi GemiBook Plus CWI620 Laptop (Intel Celeron N100/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹21,990",
        "rating": "4.35",
        "specScore": "46",
        "features": [
            "12th Gen Intel Celeron N100",
            "Quad Core, 4 Threads",
            "8 GB LPDDR5 RAM",
            "256 GB SSD",
            "Intel Integrated UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqZeImAxPW4EYC4hrhArnrysuhyihDRPw1lXJVX-h-hrhhaFhrhrhhacBrWahrhrBi5CQlTTPWFhrFB5ql7raEEzSg9P"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJ69sklFG-w280-h280/lenovo-legion-y9000k.webp",
        "productName": "Lenovo Legion Y9000K 2024 Gaming Laptop (14th Gen Core i9/ 64GB/ 2TB SSD/ Win11/ 16GB Graph)",
        "price": "₹3,49,990",
        "rating": "4.15",
        "specScore": "92",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "64 GB DDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "16 inches, 3200 x 2000 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DLenovo%2520Legion%2520Y9000K%25202024%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252064GB%252F%25202TB%2520SSD%252F%2520Win11%252F%252016GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifxP796vc-w280-h280/msi-prestige-16-ai-s.webp",
        "productName": "MSI Prestige 16 AI Studio B1VFG 2024 Laptop ( Intel Core Ultra 9/ 32GB/ 1TB SSD/ Win11/ 8GB Graphics)",
        "price": "₹1,87,990",
        "rating": "4.4",
        "specScore": "83",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB~qnwWfEY3Ewmg9hrhArnrysuhyihDRPwzz-4G0Jh-hrhhaFhrhrhhacBrWahrhrBi5F2yIWHIDhrFB5zkmbIy0rg-un"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0XFZsPUc-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 360 NP750QGK-KG3IN Laptop (Intel Core 7 Processor 150U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,33,990",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJX03dnB_4mCjPQxACWhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcZbPc54cbcYuAtcAs3acGc5bW6c5U6cuBG4PNWOcTWZYuh-hrhhaFhrhrhhacBrWahrhrBi5WXsZNg3ahrFB5QXGIUZrvsjPo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0XFZsPUc-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 360 NP750QGK-KG1IN Laptop (Intel Core 5 Processor 120U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,09,990",
        "rating": "4.6",
        "specScore": "57",
        "features": [
            "Intel Core 5 Processor Series 1 120U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJjvjG3zpB179jtb7IzhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcZbPc54cbcYuAtcAs3ac4c5bW6c45oW6cuBG4PNWOcTW5Yuh-hrhhaFhrhrhhacBrWahrhrBi5T3i4CoP5hrFB51_kVmiaz~nJZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i0XFZsPUc-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 360 NP750QGK-KG2IN Laptop (Intel Core 7 Processor 150U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,17,990",
        "rating": "4.55",
        "specScore": "59",
        "features": [
            "Intel Core 7 Processor Series 1 150U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Graphics",
            "15.6 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJX03mtqA036y2fdi-ChrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcZbPc54cbcYuAtcAs3acGc5bW6c45oW6cuBG4PNWOcTWoYuh-hrhhaFhrhrhhacBrWahrhrBi5nTtFn5rQhrFB5zqlgG8fsJUCJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUNeywWs1-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 360 NP960QGK-KG1IN Laptop (Intel Core Ultra 7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,58,990",
        "rating": "4.5",
        "specScore": "69",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJjvjK8za3R23XNRjlihrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3scZbPc5bcYuAtcCTU3rcGc5bW6c45oW6cuBlbPNWOcTW5Yuh-hrhhaFhrhrhhacBrWahrhrBi5BiYrZbHWhrFB5GlWvsYWXr2aB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibbqQF81X-w280-h280/dell-inspiron-5620-i.webp",
        "productName": "Dell Inspiron 5620 ICC-C783534WIN8 Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹61,399",
        "rating": "4.2",
        "specScore": "66",
        "features": [
            "12th Gen Intel Core i5 1240P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "16 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY9WPlO-TO_5sbdhrhAgTYBOr3Uh7iaTTcYuFBY3suc4boPcYuUaTcAs3acY4c5oUtcWauc5oZ4Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacTrBUshDhDh8lXg6ggXHbZaoAhmBYihkwkp7_.p1VSp~z.oVhrhhaFhrhrhhacBrWahrhrBi5PT32UGOghrFB5jpxqF1aTOJN4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i5ifs85et-w280-h280/msi-prestige-16-ai-s.webp",
        "productName": "MSI Prestige 16 AI Studio B1VFG Laptop ( Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11/ 8GB Graphics)",
        "price": "₹1,67,990",
        "rating": "4.15",
        "specScore": "81",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXNSXXPfHm2B_p-aDEKhrhAgTYBOr3Uh7nFYcB3aFUYWac5bcrYcFUCiYscYuUaTcAs3acCTU3rcGc544tcZocW6c5cU6cFFic8Yuis8Fc55ctsnacXcW6cW3rBtYAFc652gWcUtYucTYWtUcTrBUshDhDh86G5i55gPbiGXrhmBYihkwkp7_pzj.4G1wSREhrhhaFhrhrhhacBrWahrhrBi5YQ6lDuP3hrFB5qW3X_tnapJ2G"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-id8jFLoq0-w280-h280/msi-modern-14-d13mg.webp",
        "productName": "MSI Modern 14 D13MG-072IN Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹68,990",
        "rating": "4.45",
        "specScore": "62",
        "features": [
            "13th Gen Intel Core i7 13620H",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqEwJrq5Ik.1IU_hrhArnrysuhyihDRPKoom7GKvh-hrhhaFhrhrhhacBrWahrhrBi5b5O6Cus5hrFB5BT9JY5yWqUst"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibKtzzAd3-w280-h280/msi-modern-14-d13mg.webp",
        "productName": "MSI Modern 14 D13MG-071IN Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹78,990",
        "rating": "4.7",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqr4O~BnEzGVQ0xhrhArnrysuhyihDRPKooVKvmph-hrhhaFhrhrhhacBrWahrhrBi5UH6YoN2PhrFB5SoABV0ZouXmQ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iztmkCsPL-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-51 Laptop (11th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹50,750",
        "rating": "4.25",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrzsW38gw.jOPsvVhrhAgTYBOr3Uh7rAa3crFBY3acThscYuUaTcAs3acYGc55UtcWauc55b4WGc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacrT54c45cUtYucTYWtUcTrBUshDhDh8aoZ4AlPH56iolhmBYihkwkp7_1Sb4J.4ZdoKhrhhaFhrhrhhacBrWahrhrBi5CQu3UWBrhrFB5BrUWSI1eRlG5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPvSkak0Z-w280-h280/msi-prestige-16-ai-s.webp",
        "productName": "MSI Prestige 16 AI Studio B1VEG Laptop ( Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11/ 6GB Graphics)",
        "price": "₹1,57,990",
        "rating": "4.75",
        "specScore": "80",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBp_oETS~tFt4Y8JhrhArnrysuhyihDRPwzz7ve_.h-hrhhaFhrhrhhacBrWahrhrBi5CHuliHt3hrFB5wyCqdOKSv8ju"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itYQv0Unl-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro NP960XGK-KG1IN Laptop (Intel Core Ultra 5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,33,990",
        "rating": "4.1",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJXJ.l1ZNIqgn9sSF2KhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3sc5bcYuAtcCTU3rc4c5bW6c45oW6cuBlbPDWOcOW5Yuh-hrhhaFhrhrhhacBrWahrhrBi5u4uWB6iihrFB5a1o.g_aHqekS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2EeuH5Ou-w280-h280/msi-prestige-13-ai-e.webp",
        "productName": "MSI Prestige 13 AI Evo A1MG Laptop (Intel Core Ultra 5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹98,990",
        "rating": "4.2",
        "specScore": "66",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "13.3 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIYmeJ-bqnd17eJhrhArnrysuhyihDRPw0ZfZvX5h-hrhhaFhrhrhhacBrWahrhrBi56WHysQtHhrFB5oxkj5m6q-C2w"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ik1lbLBVk-w280-h280/msi-prestige-13-ai-e.webp",
        "productName": "MSI Prestige 13 AI Evo A1MG 2024 Laptop (Intel Core Ultra 7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,12,990",
        "rating": "4.25",
        "specScore": "69",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "13.3 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBSG7TiFEdkdd9HvhrhArnrysuhyihDRPw0oe4eo1h-hrhhaFhrhrhhacBrWahrhrBi52H4OFr3AhrFB5AlZlX98rG04D"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUO90FvEe-w280-h280/msi-prestige-16-ai-e.webp",
        "productName": "MSI Prestige 16 AI Evo  B1MG Laptop ( Intel Core Ultra 7/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹1,17,990",
        "rating": "4.25",
        "specScore": "70",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Arc",
            "16 inches, 2561 x 1600 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_ZwDwOen9UuepRIhrhArnrysuhyihDRPw0Z_-mdoh-hrhhaFhrhrhhacBrWahrhrBi5B8WrtiGyhrFB5_UwPCmwbZaz-"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZ7GMvOb4-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 14 NP940XGK-KG2IN Laptop (Intel Core Ultra 7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,34,990",
        "rating": "4",
        "specScore": "66",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJjvjR4ODJIuy8ljsjKhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3sc5HcYuAtcCTU3rcGc5bW6c45oW6cuBlHPDWOcOWoYuh-hrhhaFhrhrhhacBrWahrhrBi5aHQPQH5bhrFB5qivHEET8gWOJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVqBjkwKX-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro NP960XGK-KG2IN Laptop (Intel Core Ultra 7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,44,990",
        "rating": "4.15",
        "specScore": "68",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXCG5CZfWROiSHWtjROhrhAgTYBOr3Uh7FrnFCuWcWrTrDIc6ssOHcB3sca2scYuUaTcAs3acCTU3rcGc544tc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacuBlbPDWOcOWoYucuBlbPDWOcTWoYucUtYucTYWtUcTrBUshDhDh8igPZHHrlZai5ghmBYihkwkp7foSHeeffbXK_hrhhaFhrhrhhacBrWahrhrBi52B4uYDWyhrFB5dAUZ0Kke_22T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iZ7GMvOb4-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 14 NP940XGK-KS1IN Laptop (Intel Core Ultra 5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,23,990",
        "rating": "4.45",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJje.WyOzzIFTfa0WylhrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3sc5HcYuAtcCTU3rc4c5bW6c45oW6cuBlHPDWOcOW5Yuh-hrhhaFhrhrhhacBrWahrhrBi5b3auOAybhrFB5WbgTge9x0-Fy"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iW13QMLmV-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 14 NP940XGK-KG3IN Laptop (Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,66,990",
        "rating": "4.75",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12HZBlRwtJjvjqySGX8H8R~AlD5hrhAFrnFCuWh7Yuh-AsnBChUFh-WrTrDIc6ssOh-WrTrDIc6ssOHcB3sc5HcYuAtcCTU3rcGcZoW6c5U6cuBlHPDWOcOWZYuh-hrhhaFhrhrhhacBrWahrhrBi5CHOI3FnghrFB52ET-fjz7B97n"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-itYQv0Unl-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro NP960XGK-KG3IN Laptop (Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11)",
        "price": "₹1,76,990",
        "rating": "4.2",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXCG5DDHButCK-IX0IfhrhAgTYBOr3Uh7FrnFCuWcWrTrDIc6ssOHcB3sca2scYuUaTcAs3acCTU3rcGc544tcZocW6c5cU6cFFic8Yuis8Fc55ctsnacuBlbPDWOcOWZYucuBlbPDWOcTWZYucUtYucTYWtUcTrBUshDhDh8oa6AgXoAXaP4ohmBYihkwkp7foSHR~E71RE4hrhhaFhrhrhhacBrWahrhrBi5igHOWt3uhrFB5ErV06GKXnW7z"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-irs7PgwSN-w280-h280/asus-rog-strix-scar.webp",
        "productName": "Asus ROG Strix SCAR 16 2024 G634JZR-CM932WS Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ 12GB Graph)",
        "price": "₹2,91,000",
        "rating": "4.55",
        "specScore": "91",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "12 GB NVIDIA GeForce RTX 4080",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_e0dJTPPjT~z8PuhrhArnrysuhyihDRPw05G~K57h-hrhhaFhrhrhhacBrWahrhrBi5GuX5Y5OChrFB5T7HHymgsTm5l"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLBfJPgx8-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "Asus VivoBook 15 X1500EA-EJ111WS Laptop (Intel Pentium Gold/ 8GB/ 256GB SSD/ Win11)",
        "price": "₹25,985",
        "rating": "4.55",
        "specScore": "47",
        "features": [
            "Intel Pentium Gold 7505",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq4SxmVAgUJy-BwhrhArnrysuhyihDRPwv.4-SX_h-hrhhaFhrhrhhacBrWahrhrBi5AT6PFHAThrFB5AgTRBZCHK-EV"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-il5xYon40-w280-h280/acer-nitro-v-anv15-5.webp",
        "productName": "Acer Nitro V ANV15-51 Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 4GB Graph)",
        "price": "₹69,990",
        "rating": "4.2",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwsUf2VCmZr~3g0hrhArnrysuhyihDRPw~1oovofh-hrhhaFhrhrhhacBrWahrhrBi58A5ByayGhrFB5y.REXmKNC.Vp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJYAIku7T-w280-h280/asus-zenbook-14-oled.webp",
        "productName": "Asus Zenbook 14 OLED 2024 UX3405MA-PZ552WS Laptop (Intel Core Ultra 5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,07,990",
        "rating": "4.1",
        "specScore": "63",
        "features": [
            "Intel Core Ultra 5 Series 1 125H",
            "14 Cores (4P + 8E + 2LP-E), 18 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9BBR10dVKg3fi_DkhrhArnrysuhyihDRPKXldzb0.h-hrhhaFhrhrhhacBrWahrhrBi5lbFUlCgWhrFB50P6nEf8nAKVN"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ilvRDgsY7-w280-h280/asus-zenbook-14-oled.webp",
        "productName": "Asus Zenbook 14 OLED 2024 UX3405MA-PZ752WS Laptop (Intel Core Ultra 7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,21,899",
        "rating": "4.15",
        "specScore": "64",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf9B3HudRfQ_lla.xGhrhArnrysuhyihDRPKXlzzb0Vh-hrhhaFhrhrhhacBrWahrhrBi56o8nWt4BhrFB5tOy2GAof78bm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i47lVGts5-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo ThinkPad E14 21JKS0UA00 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹70,985",
        "rating": "4.05",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwNtB2Z9P7XQemzhrhArnrysuhyihDRPwefeZz1eh-hrhhaFhrhrhhacBrWahrhrBi53taTUs55hrFB5vYPjZrTg3.-0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAx4r5Z5M-w280-h280/hp-14-ew0153tu-lapto.webp",
        "productName": "HP 14-ew0153TU Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹92,999",
        "rating": "4.35",
        "specScore": "60",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Integrated Intel Iris Xe",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEKxZme_Fjj4mXYhrhAgTYBOr3Uh7tBcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5Hca8P54ZUCcUtYucTYWtUcTrBUshDhDh8lXXGbPZAiZoZ6hmBYihkwkp7fjpljl~p-.SjhrhhaFhrhrhhacBrWahrhrBi5HZOUNtlghrFB5Q-IYQiPHEloq"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3sviBMxO-w280-h280/hp-omen-16-xd0010ax.webp",
        "productName": "HP Omen 16-xd0010AX Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,11,720",
        "rating": "4.5",
        "specScore": "75",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXsmGe1Udmt5GYtdATShrhAgTYBOr3Uh7tBcsh2crnic3IyaucGciCrTcAs3acGXHPtFc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcHP4Pc5bcDiPP5PrDcWrnhNcTrBUshDhDh8lgGGaPaHgaaolhmBYihkwkpSfXV0SKeKvHvfhrhhaFhrhrhhacBrWahrhrBi5rbri2A6AhrFB5vuJBZRaPd5Nn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9SmpIa1y-w280-h280/infinix-inbook-y4-ma.webp",
        "productName": "Infinix INBook Y4 Max Series YL613 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹49,990",
        "rating": "4.35",
        "specScore": "54",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "16 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrznDzswormCKJI8hrhAgTYBOr3Uh7YugYuYDcIHcnrDcFa3YaFcYuUaTcAs3acYGc5ZUtcWauc5Z44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacITb5ZcUtYucTYWtUcTrBUshDhDh8ZAarXibHPZ4lAhmBYihkwkp7JJRv~V7.KeE_hrhhaFhrhrhhacBrWahrhrBi5WDNnu3AuhrFB57JyDtUjqyKwU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuoh3JmE2-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 3 Chromebook 14IAN8 83BN001PHA Laptop (Intel Pentium N100/ 4GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹28,190",
        "rating": "4.6",
        "specScore": "35",
        "features": [
            "Intel Pentium N100",
            "Quad Core, 4 Threads",
            "4 GB LPDDR4X RAM",
            "128 GB Hard Disk",
            "Intel UHD Graphics",
            "14 inches, 1366 x 768 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtIKVEgvbIwJV-2hrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcBauUYCncNCricAs3acu5PPcHcW6c5oXcW6cannAcFUs3rWacAt3snacsFc5HYruXcAt3sna6ssOcTrBUshDhDh8GAPA4XZoPooPihmBYihkwkp7zofZKSwb~dHvhrhhaFhrhrhhacBrWahrhrBi5TFobZIOshrFB5_d1iG4FCmUeG"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqXG8WBxA-w280-h280/lenovo-loq-15irx9-83.webp",
        "productName": "Lenovo LOQ 15IRX9 83DV007HIN Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,01,490",
        "rating": "4",
        "specScore": "65",
        "features": [
            "13th Gen Intel Core i7 13650HX",
            "14 Cores (6P + 8E)",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBxO_jaJ90bWECEzhrhArnrysuhyihDRPwvK0md7mh-hrhhaFhrhrhhacBrWahrhrBi5HYnDHBylhrFB52pj9zDqH5dAX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikmOqyMpx-w280-h280/hp-pavilion-15-eh303.webp",
        "productName": "HP Pavilion 15-eh3039AU Laptop ( AMD Ryzen 5 7530U/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4.1",
        "specScore": "62",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwtaZ.0WPa5EXYXhrhArnrysuhyihDRPwvxoZXKeh-hrhhaFhrhrhhacBrWahrhrBi5QiCG83NThrFB5xuG44x_~IHvp"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivsUe0UUZ-w280-h280/asus-tuf-gaming-f17.webp",
        "productName": "Asus TUF Gaming F17 FX706HF-HX044WS Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹51,985",
        "rating": "4.15",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i5 11400H",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "17 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.af67PU6oBJZX24uF8hrhArnrysuhyihDRPwfw7-1._h-hrhhaFhrhrhhacBrWahrhrBi5gDtU4oGahrFB5nlX488RddUJ4"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXpu8urP5-w280-h280/hp-15s-fr5010tu-lapt.webp",
        "productName": "HP 15s-fr5010TU Laptop (12th Gen Core i5/8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹46,023",
        "rating": "4.25",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqSR-fyG-9A...thrhArnrysuhyihDRPwvx5Rf_lh-hrhhaFhrhrhhacBrWahrhrBi5ZNbWnuWghrFB5yPG9kjzKV-EP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iMOA497tU-w280-h280/hp-245-g9-841w7pa-la.webp",
        "productName": "HP 245 G9 841W7PA Laptop (AMD Ryzen 3 3250U/ 8 GB RAM/ 512 GB SSD/ DOS)",
        "price": "₹25,980",
        "rating": "4.55",
        "specScore": "50",
        "features": [
            "3rd Gen AMD Ryzen 3 3250U",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "14 inches, 1366 x 768 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI5OvTsp0XxlH9thrhArnrysuhyihDRPwvKewlwwh-hrhhaFhrhrhhacBrWahrhrBi5tHooABBGhrFB5Q9FJGrfxf6.g"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iA7Ei9xYE-w280-h280/asus-chromebook-cm14.webp",
        "productName": "Asus Chromebook CM14 CM1402CM2A-EK0085 Laptop (MediaTek Kompanio 520/ 8GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹28,461",
        "rating": "4.65",
        "specScore": "27",
        "features": [
            "MediaTek Kompanio Kompanio 520",
            "Octa Core",
            "8 GB LPDDR4X RAM",
            "128 GB Hard Disk",
            "Arm Mali G52 MC2 2EE",
            "14 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw~tSiKp_2zGIwDhrhArnrysuhyihDRPw~mvSeeZh-hrhhaFhrhrhhacBrWahrhrBi5ylUNP3bDhrFB5.7Puf.DuEoXW"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQpRCUoXJ-w280-h280/lenovo-loq-15iax9i-8.webp",
        "productName": "Lenovo LOQ 15IAX9I 83FQ0009IN Gaming Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹56,490",
        "rating": "4.25",
        "specScore": "57",
        "features": [
            "12th Gen intel Core i5 12450HX",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB Intel Integrated ARC A530M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqdq-X4-wjdU-kNhrhArnrysuhyihDRPwvK0xVbRh-hrhhaFhrhrhhacBrWahrhrBi5Z6H3PC4lhrFB5RKV4frxqWntC"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGDFWFf1V-w280-h280/hp-spectre-x360-16-a.webp",
        "productName": "HP Spectre x360 16-aa0665TU Laptop (Intel Core Ultra 7/ 32GB/ 2TB SSD/ Win11 Home)",
        "price": "₹1,81,456",
        "rating": "4.2",
        "specScore": "80",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "2 TB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_RxSHqH5s0zH0VRhrhArnrysuhyihDRPwvV1l.pmh-hrhhaFhrhrhhacBrWahrhrBi56nyoZrDohrFB5~55J6psEs0HS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWY3wn6S7-w280-h280/hp-spectre-x360-14-e.webp",
        "productName": "HP Spectre x360 14-eu0556TU Laptop (Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,62,990",
        "rating": "4.2",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIAv9JIjY4X~AJ_RDZmjShrhAgTYBOr3Uh7tBcFBaAU3acDZbPcYuUaTcAs3acCTU3rcGc544tcZocW6c5cU6cFFic8Yuis8Fc55ctsnac5HcaCP44bUCcoc5cTrBUshDhDh86gl55HgoXirobhmBYihkwkp7J0RR77fHxe.1hrhhaFhrhrhhacBrWahrhrBi52Q8XHya2hrFB5~DrHubqt~WXf"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izaoH2L1O-w280-h280/acer-aspire-lite-al1.webp",
        "productName": "Acer Aspire Lite AL15-52 15 Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹44,985",
        "rating": "4.35",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq766ws9v7rKH_bhrhArnrysuhyihDRPw~0~0v~fh-hrhhaFhrhrhhacBrWahrhrBi5Bg83slQ2hrFB5RKXPJT0gmS1X"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i4TyOVy35-w280-h280/hp-spectre-x360-14-e.webp",
        "productName": "HP Spectre x360 14-eu0666TU Laptop (Intel Core Ultra 7/ 32GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,62,990",
        "rating": "4.65",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5x RAM",
            "1 TB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~mC3ixm_63nnIznhrhAgTYBOr3Uh7tBcFBaAU3acDZbPcYuUaTcAs3acCTU3rcGc544tcZocW6c5cU6cFFic8Yuis8Fc55ctsnac5HcaCPbbbUCcoc5cTrBUshDhDh8HaiH4abgbX6bXhmBYihkwkp7J0RR7bepf~.ShrhhaFhrhrhhacBrWahrhrBi5IrZZ6DUyhrFB5KBIvI2pssQqn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iVA0u4bdm-w280-h280/msi-titan-18-hx-gami.webp",
        "productName": "MSI Titan 18 HX Gaming Laptop (14th Gen Core i9/ 32GB/ 2TB SSD/ Win11 Home/ RTX 4090)",
        "price": "₹4,99,990",
        "rating": "4.2",
        "specScore": "87",
        "features": [
            "14th Gen Intel Core i9 14900HX",
            "32 GB DDR5 RAM",
            "2 TB SSD",
            "16 GB NVIDIA GeForce RTX 4090",
            "18 inches, 3840 x 2400 pixels",
            "Windows 11 OS",
            "2 Year Warranty",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMSI%2520Titan%252018%2520HX%2520Gaming%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25202TB%2520SSD%252F%2520Win11%2520Home%252F%2520RTX%25204090)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-isIoS0mJZ-w280-h280/acer-nitro-v-2023-an.webp",
        "productName": "Acer Nitro V 2023 ANV15-51 Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹81,999",
        "rating": "4.45",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FI.SWD2b~lmnfIohrhArnrysuhyihDRPw~1Hz5-0h-hrhhaFhrhrhhacBrWahrhrBi5I4Uo333OhrFB5GgF_tn0IAXor"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ihnZ843Jg-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82X60013IN Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹41,400",
        "rating": "4.45",
        "specScore": "46",
        "features": [
            "13th Gen Intel Core i3 1305U",
            "5 Cores (1P + 4E), 6 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Integrated Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqxZGmidr8C8A9ThrhArnrysuhyihDRPwvX.50RKh-hrhhaFhrhrhhacBrWahrhrBi56iaH3sDrhrFB5PA1Y_8.Ao9Qg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iolIUzHMn-w280-h280/avita-liber-liber-e.webp",
        "productName": "Avita Liber Liber E AM14A2INL54F Laptop (AMD Ryzen 5 5500U/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹25,990",
        "rating": "4.75",
        "specScore": "45",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "AMD Radeon",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rw1J9R86RgqmKErhrhArnrysuhyihDRPw1lp0mpfh-hrhhaFhrhrhhacBrWahrhrBi5ttt4ZQOuhrFB5g4t5agDiHGz."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivl17P4n6-w280-h280/dell-g15-5530-gaming.webp",
        "productName": "Dell G15-5530 Gaming Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹76,999",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i5 13450HX",
            "10 Cores (6P + 4E), 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrObuYr8_wDHvsK0hrhAgTYBOr3Uh7iaTTcYuUaTcAs3acY4c5ZUtcWauc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcZP4PcW54c44ZPcWrnhNcTrBUshDhDh8aZralgoGlog5rhmBYihkwkpSZ7fpRx.G~-EGhrhhaFhrhrhhacBrWahrhrBi55QHBWrQNhrFB5YeDNePI9YTbK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ijvcepm4I-w280-h280/dell-g16-7630-gaming.webp",
        "productName": "Dell ‎G16 7630 Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,95,590",
        "rating": "4.3",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJaoQ4oXaU8ADrzOhrhArnrysuhyihDRPwKRdGwdSh-hrhhaFhrhrhhacBrWahrhrBi5bYouWyWThrFB5NDvk6CNlGniZ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip4GjOZQm-w280-h280/msi-prestige-13-ai-e.webp",
        "productName": "MSI Prestige 13 AI Evo A1M Laptop (Intel Core Ultra 7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹1,13,999",
        "rating": "4.4",
        "specScore": "64",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "13.3 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "2 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DMSI%2520Prestige%252013%2520AI%2520Evo%2520A1M%2520Laptop%2520(Intel%2520Core%2520Ultra%25207%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iefz72otf-w280-h280/hp-omen-16-wf0054tx.webp",
        "productName": "HP Omen 16-wf0054TX Gaming Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home/ 8GB Graph)",
        "price": "₹1,24,409",
        "rating": "4.75",
        "specScore": "73",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJ09oE1psEEHqJ_lhrhArnrysuhyihDRPww-zZ.o_h-hrhhaFhrhrhhacBrWahrhrBi5ul6QTrnNhrFB5oFPYF9x.7_E7"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNUHe2IBb-w280-h280/infinix-inbook-y2-pl.webp",
        "productName": "Infinix INBook Y2 Plus XL29 Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win 11 Home)",
        "price": "₹25,990",
        "rating": "4.15",
        "specScore": "44",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB LPDDR4X RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrQAUkdT1O8ztyy6hrhAgTYBOr3Uh7YugYuYDcYu6ssOcIocBTCFcoPoHcYuUaTcAs3acYZc55UtcWauc5554WHcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacDTolcUtYucTYWtUcTrBUshDhDh8Ag5ZAGaP6PAGXhmBYihkwkp70-GS.X7~xEE1hrhhaFhrhrhhacBrWahrhrBi5lPZO5ZPGhrFB5NV41VWjiv4q9"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXiI3A9XM-w280-h280/lenovo-ideapad-flex.webp",
        "productName": "Lenovo Ideapad Flex 5 14IAU7 82R700KHIN Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹53,990",
        "rating": "4.6",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDA0ZC56z_yOvWxa29hrhAA3snrh7Taus2scYiarBricgTaDc4c5HYrCGcYuUaTcAs3acYZc5oUtcWauc5HcYuAtcXW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5cYuUaTcCtic8CDWrcYBFciYFBTrIcFUs3ncW3aIcXo3GPPOtYuch-hDZPoHbohrhhaFhrhrhhacBrWahrhrBi5Zl5bnBothrFB516m~8sdmmGlI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iOoBptMBb-w280-h280/lenovo-legion-pro-5.webp",
        "productName": "Lenovo Legion Pro 5 161IRX9 Laptop (14th Gen Core i9/ 32GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,49,990",
        "rating": "4.7",
        "specScore": "69",
        "features": [
            "Intel Core i9 14900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "32 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DLenovo%2520Legion%2520Pro%25205%2520161IRX9%2520Laptop%2520(14th%2520Gen%2520Core%2520i9%252F%252032GB%252F%25201TB%2520SSD%252F%2520Win11%252F%25208GB%2520Graph)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-inIIv2Goh-w280-h280/hp-240-g9-8j0s5pa-la.webp",
        "productName": "HP 240 G9 8J0S5PA Laptop (12th Gen Core i5/ 8GB/ 512 GB SSD/ DOS)",
        "price": "₹52,799",
        "rating": "4.05",
        "specScore": "54",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1366 x 768 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgTzkJnidZZd10hrhArnrysuhyihDRPw7oo4ol_h-hrhhaFhrhrhhacBrWahrhrBi5ABI3yoDohrFB5BWjxVsq7BX2H"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibK7CKA2l-w280-h280/asus-zenbook-14-oled.webp",
        "productName": "Asus Zenbook 14 OLED UX3405 Laptop (Intel Core Ultra 9 / 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹1,49,990",
        "rating": "4",
        "specScore": "65",
        "features": [
            "Intel Core Ultra 9 Series 1 185H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "14 inches, 2880 x 1800 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DAsus%2520Zenbook%252014%2520OLED%2520UX3405%2520Laptop%2520(Intel%2520Core%2520Ultra%25209%2520%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGQUtNlCY-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Pro 360 Laptop (Intel Core Ultra 7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,99,990",
        "rating": "4.4",
        "specScore": "72",
        "features": [
            "Intel Core Ultra 7 Series 1 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "16 GB LPDDR5X RAM",
            "512 GB SSD",
            "Intel Arc Graphics",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25204%2520Pro%2520360%2520Laptop%2520(Intel%2520Core%2520Ultra%25207%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibkAmiTly-w280-h280/lenovo-thinkbook-14.webp",
        "productName": "Lenovo ThinkBook 14 21DH00C1IH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹56,750",
        "rating": "4.75",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwt.Hd5JCpWNn~vhrhArnrysuhyihDRPw-o7_0Sxh-hrhhaFhrhrhhacBrWahrhrBi5Hs6g63gQhrFB58PJjOOPpAsTO"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iu8ISScpI-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82H803HQIN Laptop (11th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹44,500",
        "rating": "4.75",
        "specScore": "60",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwrW0m~IvafZEXthrhArnrysuhyihDRPw1oVx1Vwh-hrhhaFhrhrhhacBrWahrhrBi5abZsFDaThrFB545RX9TJG9RS8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i6MOvZNjg-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3 82H803LKIN Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹48,990",
        "rating": "4.7",
        "specScore": "62",
        "features": [
            "11th Gen Intel Core i5 1155G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwAg5kdroGfux1vhrhArnrysuhyihDRPw1oSV5dXh-hrhhaFhrhrhhacBrWahrhrBi5ayC6FIuBhrFB51DiVNFIxwisn"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQEY0VepN-w280-h280/huawei-qingyun-l540.webp",
        "productName": "Huawei Qingyun L540 Laptop (Kirin 9006C/ 8 GB RAM/ 256 GB SSD/ Kirin OS)",
        "price": "₹70,499",
        "rating": "4.3",
        "specScore": "23",
        "features": [
            "Kirin 9006C",
            "8 GB  RAM",
            "256 GB SSD",
            "14 inches, 2160 x 1440 pixels",
            "Linux OS"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHuawei%2520Qingyun%2520L540%2520Laptop%2520(Kirin%25209006C%252F%25208%2520GB%2520RAM%252F%2520256%2520GB%2520SSD%252F%2520Kirin%2520OS)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iQoA3WpnB-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 Ultra Laptop (Intel Core Ultra 7 155H/ 32 GB RAM/ 1 TB SSD/ 6 GB Graphics)",
        "price": "₹2,99,999",
        "rating": "4.15",
        "specScore": "75",
        "features": [
            "Intel Core Ultra 7 155H",
            "16 Cores (6P + 8E + 2LP-E), 22 Threads",
            "32 GB LPDDR5X RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16 inches, 2880 x 1800 pixels, Touch Screen",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25204%2520Ultra%2520Laptop%2520(Intel%2520Core%2520Ultra%25207%2520155H%252F%252032%2520GB%2520RAM%252F%25201%2520TB%2520SSD%252F%25206%2520GB%2520Graphics)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJiN0hS9u-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 3i 82RK011EIN Laptop (12th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹56,990",
        "rating": "4.4",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Integrated Intel IrisXe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFe50kN4Z7xV_JHhrhAgTYBOr3Uh7Taus2scYiarBricFTYncZcYuUaTcAs3acYGc5oUtcWauc5o44Cc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54YrCGcUtYucTYWtUcTrBUshDhDh8HXrl4lHZragPHhmBYihkwkp70~of.fdRRS0-hrhhaFhrhrhhacBrWahrhrBi5X4aabQDnhrFB5TEvKTG7jTAry"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iUVmH76zG-w280-h280/lenovo-yoga-slim-6-1.webp",
        "productName": "Lenovo Yoga Slim 6 14IRH8 83E00012INLaptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹81,990",
        "rating": "4.75",
        "specScore": "59",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5X RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrOj~pXe6nSrT06uhrhAgTYBOr3Uh7Taus2scIsWrcFTYncbc8CDWrcsTaicYuUaTcAs3acY4c5ZUtcWauc5Z4PPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacXZaPPP5oYucUtYucTYWtUcTrBUshDhDh8HHo4GlioXX5XAhmBYihkwkp70Vpb.HEbJp.7hrhhaFhrhrhhacBrWahrhrBi5bHA6lgYbhrFB55tUJoArUf_ao"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWjBGd4DV-w280-h280/huawei-matebook-14s.webp",
        "productName": "Huawei MateBook 14s 2023 Laptop (13th Gen Core i9/ 16GB RAM/ 1TB SSD/ Win11 Home)",
        "price": "₹80,999",
        "rating": "4.6",
        "specScore": "68",
        "features": [
            "13th Gen Intel Core i9 13900H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB  RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14.2 inches, 2520 x 1680 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DHuawei%2520MateBook%252014s%25202023%2520Laptop%2520(13th%2520Gen%2520Core%2520i9%252F%252016GB%2520RAM%252F%25201TB%2520SSD%252F%2520Win11%2520Home)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iy90AjLcu-w280-h280/dell-inspiron-3535-l.webp",
        "productName": "Dell Inspiron 3535 Laptop (AMD Ryzen R3-7320U,/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,043",
        "rating": "4.5",
        "specScore": "50",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqjkqa2Y39mzIG6hrhArnrysuhyihDRPKXZleR~mh-hrhhaFhrhrhhacBrWahrhrBi5P33uyCTahrFB5OvaOH~9OXBCm"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3OkdKNv8-w280-h280/xiaomi-redmi-book-16.webp",
        "productName": "Xiaomi Redmi Book 16 2024 Laptop (13th Gen Core i5/ 16GB/ 512GB SSD/ Win 11)",
        "price": "₹52,990",
        "rating": "4.15",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i5 13500H",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DXiaomi%2520Redmi%2520Book%252016%25202024%2520Laptop%2520(13th%2520Gen%2520Core%2520i5%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win%252011)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifNNpcttj-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo IdeaPad Gaming 3 15IAH7 82S9017TIN Laptop (12th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹65,460",
        "rating": "4.15",
        "specScore": "61",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 3050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqea8KCK_opXmxHhrhArnrysuhyihDRPwd1xSV4ph-hrhhaFhrhrhhacBrWahrhrBi5bGCg432GhrFB5dP~fo9Z3ZHWz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-izwAaNxSK-w280-h280/dell-inspiron-7430-1.webp",
        "productName": "Dell Inspiron 7430 14 2 in 1 Laptop (13th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹58,090",
        "rating": "4.45",
        "specScore": "55",
        "features": [
            "13th Gen Intel Core i3 1315U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK46QWxI00TPrQWshrhAA3snrh7iaTTcYuFBY3sucGHZPcYuUaTcAs3acYZc5ZUtcWaucUsCAtFA3aaucUtYuchYcTYWtUcTrBUsBcXW6c45oW6cFFic8Yuis8Fc55ctsnac5HcYuAtcgCTTcticBTCFciYFBTrIcnFcsggYAacoPo5cBTrUYuCncFYThCc5c4XcOWch-hDZPH5GlhrhhaFhrhrhhacBrWahrhrBi5NGGiProChrFB5-dRqUGxm2mvg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i868WxDDI-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XF0078IN Laptop (13th Gen Core i7/ 16 GB RAM/ 1 TB SSD/ Win 11)",
        "price": "₹79,990",
        "rating": "4.45",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEHilp59X._DnsHhrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4cYuUaTcAs3acYGc5ZUtcWauc5ZGPPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5bY3TXcTrBUshDhDh8lHiG5HagrHArHhmBYihkwkp70~ofj0.e.efXhrhhaFhrhrhhacBrWahrhrBi5UulsQsbXhrFB5KghUWxVqsXk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ivRWiYRXe-w280-h280/samsung-galaxy-book.webp",
        "productName": "Samsung Galaxy Book 4 360 Laptop (13th Gen Core i7/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹1,29,900",
        "rating": "4.05",
        "specScore": "57",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "13.3 inches, 1920 x 1080 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DSamsung%2520Galaxy%2520Book%25204%2520360%2520Laptop%2520(13th%2520Gen%2520Core%2520i7%252F%252016GB%252F%2520512GB%2520SSD%252F%2520Win11)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iSlqCvLRM-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo IdeaPad Slim 5 14IAH8 83BF0043IN Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹61,490",
        "rating": "4.1",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Integrated Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq~3Zuy2pd6Io94hrhArnrysuhyihDRPwdV50z.Jh-hrhhaFhrhrhhacBrWahrhrBi52AnDI8NlhrFB5mHpQW2tjfRgB"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-in7OIYFEO-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "Lenovo Ideapad Slim 5 82XD006GIN Laptop (13th Gen Core i5/ 16 GB RAM/ 1TB SSD/ Win 11)",
        "price": "₹78,990",
        "rating": "4.45",
        "specScore": "53",
        "features": [
            "13th Gen Intel Core i5 13420H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Integrated Intel UHD Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEHRZJSe3u0po9fhrhAgTYBOr3Uh7Taus2scYiarBricFTYnc4c8CDWrcsTaicYuUaTcAs3acY4c5ZUtcWauc5ZHoPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnac5HY3TXcUtYucTYWtUcTrBUshDhDh8goiga6lgZ4iPGhmBYihkwkp70~ofJGewSzlfhrhhaFhrhrhhacBrWahrhrBi5GYUtCIaYhrFB5w3F1xsu4uPrs"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i9bWlT2dl-w280-h280/jio-jiobook-cloud-la.webp",
        "productName": "Jio JioBook Cloud Laptop (Octa Core/ 4GB/ 64GB eMMC/ JioOS)",
        "price": "₹14,999",
        "rating": "4.15",
        "specScore": "19",
        "features": [
            "Octa Core",
            "4 GB ‎LPDDR4 RAM",
            "64 GB Hard Disk",
            "11.6 inches, 1366 x 768 pixels",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DJio%2520JioBook%2520Cloud%2520Laptop%2520(Octa%2520Core%252F%25204GB%252F%252064GB%2520eMMC%252F%2520JioOS)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGUxUJ2Ay-w280-h280/dell-5530-g15-gaming.webp",
        "productName": "Dell 5530 G15 Gaming Laptop (13th Gen Core i9/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,48,690",
        "rating": "4.45",
        "specScore": "74",
        "features": [
            "13th Gen Intel Core i9 13900HX",
            "24 Cores (8P + 16E), 32 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4060",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJflDVJOOX2HxE3thrhArnrysuhyihDRPwd5mG_eoh-hrhhaFhrhrhhacBrWahrhrBi5TXrNlCoghrFB5e4dU0JBBjRZ_"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJ08jhdTN-w280-h280/dell-latitude-3520-d.webp",
        "productName": "Dell Latitude 3520 DLCK3520BL Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Ubuntu)",
        "price": "₹35,500",
        "rating": "4.5",
        "specScore": "48",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Ubuntu OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?url=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3DDell%2520Latitude%25203520%2520DLCK3520BL%2520Laptop%2520(11th%2520Gen%2520Core%2520i3%252F%25208GB%252F%2520512GB%2520SSD%252F%2520Ubuntu)%26rh%3Dp_n_availability%253A1318485031"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibtieEwq9-w280-h280/hp-250-g9-95x40pa-la.webp",
        "productName": "HP 250 G9 95X40PA Laptop (12th Gen Core i7/ 8GB/ 512 GB SSD/ DOS)",
        "price": "₹65,999",
        "rating": "4.2",
        "specScore": "48",
        "features": [
            "12th Gen Intel Core i7 1255U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1920 x 1080 pixels",
            "DOS OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Rwu49YnXNsmmunlhrhArnrysuhyihDRPwd7fd0m7h-hrhhaFhrhrhhacBrWahrhrBi5aogb3D4rhrFB5wIrp1g_m9jkF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ict2La4FS-w280-h280/dell-inspiron-3520-i.webp",
        "productName": "Dell Inspiron 3520 IN3520RVTGV001ORB1 Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹34,390",
        "rating": "4.3",
        "specScore": "45",
        "features": [
            "11th Gen Intel Core i3 1115G4",
            "Dual Core, 4 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYopEIOP~ywf0GDhrhAgTYBOr3Uh7iaTTcTrUYUCiacYuUaTcAs3acYZc55UtcWauc5554WHcXcW6c45ocW6cFFic8Yuis8Fc55cB3scZ4oPcTrBUshDhDh8PgiPrri55aPglhmBYihkwkp7effVo~S7q7-lhrhhaFhrhrhhacBrWahrhrBi5Q2BNoIu8hrFB5vab~U8UtpRpP"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ip384XfpC-w280-h280/lenovo-thinkpad-e14.webp",
        "productName": "Lenovo Thinkpad E14 G4 21E3S00P00 Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹67,999",
        "rating": "4.4",
        "specScore": "59",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "DOS OS",
            "Backlit Keyboard"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwuyEkxukp~.9uRhrhArnrysuhyihDRPRzGe0bwJh-hrhhaFhrhrhhacBrWahrhrBi5iiyQn65ahrFB5GNJny5q7ByJx"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuhzLGvaz-w280-h280/lenovo-thinkpad-x1-c.webp",
        "productName": "Lenovo ThinkPad X1 Carbon 21HMS00000 Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Pro)",
        "price": "₹2,09,990",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 1355U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1200 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvREvJQk1DaHW9eI~quxhrhArnrysuhyihDRPwplZ7xbHh-hrhhaFhrhrhhacBrWahrhrBi5aU6yiBtChrFB5ifCtysiml6VF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ikwnViJtB-w280-h280/avita-liber-am15a2in.webp",
        "productName": "Avita Liber AM15A2INT56F Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹25,990",
        "rating": "4.05",
        "specScore": "46",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB  RAM",
            "512 GB SSD",
            "Intel Integrated Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uq4SmW.f4nx2pajhrhArnrysuhyihDRPw1ld0vKzh-hrhhaFhrhrhhacBrWahrhrBi5BBDgy4QnhrFB58BsSjDAZGX9A"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGjivyBcu-w280-h280/acer-travelmate-p2-t.webp",
        "productName": "Acer TravelMate P2 TMP214-53 14 Business Laptop (11th Gen Core i7/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹42,980",
        "rating": "4.2",
        "specScore": "59",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated Iris Xe",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FIwj6DsdYDKl-y.hrhArnrysuhyihDRPwSvd.ZGmh-hrhhaFhrhrhhacBrWahrhrBi5aPNlWyDlhrFB5UeDHXNOFCla5"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iInaH6OZT-w280-h280/hp-victus-15-fa1145t.webp",
        "productName": "HP Victus 15-fa1145TX Gaming Laptop (12th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹68,990",
        "rating": "4.55",
        "specScore": "68",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrO5s.S1Uifuwx8yhrhAgTYBOr3Uh7tBc2YAUCFcYuUaTcAs3acY4c5oUtcWauc5oH4Ptc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacHcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcoP4Pc4PcUWBc54cgr55H4UDcWrnhNcTrBUshDhDh8GZHZiar6riXr6hmBYihkwkp7e0Hv4Kj.fepqhrhhaFhrhrhhacBrWahrhrBi5I5PY2Yg2hrFB5KHRd-ZFI1A29"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iiLxIA90M-w280-h280/hp-probook-440-g8-7l.webp",
        "productName": "HP ProBook 440 G8 7L375PA Notebook PC (11th Gen Core i7/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹97,499",
        "rating": "4.65",
        "specScore": "63",
        "features": [
            "11th Gen Intel Core i7 1165G7",
            "Quad Core, 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RK4EpP5QKI020omhrhArnrysuhyihDRPwofV7bGlh-hrhhaFhrhrhhacBrWahrhrBi5ygCiFlBDhrFB5ZbZwD2Y4vkNz"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iC77Mzps9-w280-h280/avita-pura-s101-lapt.webp",
        "productName": "Avita Pura S101 Laptop (Celeron N4020/ 8GB/256GB SSD/ Win11 Home)",
        "price": "₹16,990",
        "rating": "4.6",
        "specScore": "36",
        "features": [
            "Intel Celeron  N4020",
            "Dual Core, 2 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel Integrated UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_FD8-EZDvfiC3O.shrhArnrysuhyihDRPw1ld0Jd-h-hrhhaFhrhrhhacBrWahrhrBi5rXClIFtChrFB5g5ukWu.eXZXK"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ipO0D0DmL-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Pro/ 18GB/ 512GB SSD/ macOS)",
        "price": "₹2,34,990",
        "rating": "4.2",
        "specScore": "56",
        "features": [
            "Apple M3 Pro",
            "12 Cores (6P + 6E)",
            "18 GB  RAM",
            "512 GB SSD",
            "18 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_CSq6-ymykoF2R8hrhArnrysuhyihDRPwp4~75f5h-hrhhaFhrhrhhacBrWahrhrBi5bXo5nTIyhrFB5ZgSXm2t27C~O"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iWm0h85E0-w280-h280/apple-macbook-pro-14.webp",
        "productName": "Apple MacBook Pro 14 2023 Laptop (Apple M3/ 8GB/ 1TB SSD/ macOS)",
        "price": "₹1,78,590",
        "rating": "4.1",
        "specScore": "52",
        "features": [
            "Apple M3",
            "Octa Core (4P + 4E)",
            "8 GB  RAM",
            "1 TB SSD",
            "10 Core GPU",
            "14.2 inches, 3024 x 1964 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_Q0Tyrak7k7C2GehrhArnrysuhyihDRPwp4vHx14h-hrhhaFhrhrhhacBrWahrhrBi5tiPAI3aBhrFB5KJpan_Xk~5uk"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1G12azTJ-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Max/ 36GB/ 1TB SSD/ macOS)",
        "price": "₹3,19,900",
        "rating": "4",
        "specScore": "64",
        "features": [
            "Apple M3 Max",
            "14 Cores (10P + 4E)",
            "36 GB  RAM",
            "1 TB SSD",
            "30 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-fXVOwdE4BofC11xhrhArnrysuhyihDRPwp4vlv-Vh-hrhhaFhrhrhhacBrWahrhrBi5l8B8gNrghrFB5KKWrN9I.G9p."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iGgF0yQhv-w280-h280/apple-macbook-pro-16.webp",
        "productName": "Apple MacBook Pro 16 2023 Laptop (Apple M3 Pro/ 36GB/ 512GB SSD/ macOS)",
        "price": "₹2,72,649",
        "rating": "4.65",
        "specScore": "62",
        "features": [
            "Apple M3 Pro",
            "12 Cores (6P + 6E)",
            "36 GB  RAM",
            "512 GB SSD",
            "18 Core GPU",
            "16.2 inches, 3456 x 2234 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_yP7jNDHTHaOYywhrhArnrysuhyihDRPwp4~JK4~h-hrhhaFhrhrhhacBrWahrhrBi5AtGBs2HAhrFB5y~2GYlvfIZxX"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iNh6upGAr-w280-h280/apple-macbook-pro-14.webp",
        "productName": "Apple MacBook Pro 14 2023 Laptop (Apple M3 Max/ 36GB/ 1TB SSD/ macOS)",
        "price": "₹2,99,990",
        "rating": "4.2",
        "specScore": "63",
        "features": [
            "Apple M3 Max",
            "14 Cores (10P + 4E)",
            "36 GB  RAM",
            "1 TB SSD",
            "30 Core GPU",
            "14.2 inches, 3024 x 1964 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXFwvxjijqt02HU3HFbhrhAgTYBOr3Uh7rBBTacoPoZcnrA6ssOcB3scnZcnrDcZbcW6c5cU6cFFicnrAsFcFsusnrcn3D4Ztucrh-hDh8laHorbHiXX66GhmBYihkwkp7Ez_GfVzKpz7~hrhhaFhrhrhhacBrWahrhrBi5tCUgrrn4hrFB57SOxJp4dAr4k"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iq7ZH7Rgx-w280-h280/apple-macbook-pro-14.webp",
        "productName": "Apple MacBook Pro 14 2023 Laptop (Apple M3 Pro/ 18GB/ 1TB SSD/ macOS)",
        "price": "₹2,25,690",
        "rating": "4.35",
        "specScore": "56",
        "features": [
            "Apple M3 Pro",
            "12 Cores (6P + 6E)",
            "18 GB  RAM",
            "1 TB SSD",
            "18 Core GPU",
            "14.2 inches, 3024 x 1964 pixels",
            "Mac OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRf-_UGRiWOeuYlwV.HhrhArnrysuhyihDRPwp4vo~_eh-hrhhaFhrhrhhacBrWahrhrBi5yGCuoD38hrFB5QiVO0UC7bmpt"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iwI8yFYDA-w280-h280/lenovo-ideapad-gamin.webp",
        "productName": "Lenovo Ideapad Gaming 3 15ARH7 82SB00QJIN Laptop  (AMD Ryzen 5 7535HS / 16GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹68,990",
        "rating": "4.35",
        "specScore": "65",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "16 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYpZ0nn8Q~F15W-hrhAgTYBOr3Uh7Taus2scrnic3Iyauc4c5bcW6c45ocW6cFFic8Yuis8Fc55ctsnacHcW3rBtYAFcu2YiYrcWags3Aac3UDcu2YiYrcoP4PcXoF6PPNQYucWrnhNcTrBUshDhDh8ZiZAg4PGXHoXrhmBYihkwkp7EX_0dwbS~ESdhrhhaFhrhrhhacBrWahrhrBi5D83rAHbUhrFB5gbmYQu9HHWie"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-io1UKfSnP-w280-h280/lenovo-yoga-slim-7i.webp",
        "productName": "Lenovo Yoga Slim 7i Carbon 13IRP8 83AY003CIN Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹1,23,190",
        "rating": "4.3",
        "specScore": "64",
        "features": [
            "13th Gen Intel Core i7 1360P",
            "12 Cores (4P + 8E), 16 Threads",
            "16 GB LPDDR5 RAM",
            "1 TB SSD",
            "Intel Integrated Iris Xe",
            "13.3 inches, 2560 x 1600 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpB9kGXnU.uodEEXshrhArnrysuhyihDRPwSv~-X1Jh-hrhhaFhrhrhhacBrWahrhrBi5tPOgBy5AhrFB58_gRR0SxoTK1"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iPb2wI6sF-w280-h280/hp-15s-fq2510tu-lapt.webp",
        "productName": "HP 15s-fq2510tu Laptop (11th Gen Core i5/ 16GB/ 512GB SSD/ Win11 Home)",
        "price": "₹49,000",
        "rating": "4.45",
        "specScore": "60",
        "features": [
            "11th Gen Intel Core i5 1135G7",
            "Quad Core, 8 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFYjkKS7aO4~EelThrhAgTYBOr3Uh7tBcoPoZcTrBUsBc6huTYUcOaI6sr3icYuUaTcAs3acY4c55UtcWauc5bcW6c45ocW6cFFic8Yuis8Fc55ctsnac54FcgNo45PUCcUtYucTYWtUh-hDh8GiH4GG5ZHa46AhmBYihkwkp7EpXEV-R_XfVphrhhaFhrhrhhacBrWahrhrBi5C3sGWa8NhrFB5qfAfOoeANxim"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ibbcXaEtW-w280-h280/asus-chromebook-cx15.webp",
        "productName": "Asus Chromebook CX1500CKA-EJ0247 Laptop (Celeron N4500/ 8GB/ 128GB eMMC/ Chrome OS)",
        "price": "₹19,990",
        "rating": "4.4",
        "specScore": "32",
        "features": [
            "Intel Celeron N4500",
            "Dual Core, 2 Threads",
            "8 GB LPDDR4X RAM",
            "128 GB Hard Disk",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Chrome OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFtUZEdE51NRv5lShrhAgTYBOr3Uh7rFCFcAt3sna6ssOcYuUaTcAaTa3suciCrTcAs3acuH4PPcXcW6c5oXcW6cannAcFUs3rWacAt3snacsFcAD54PPAOrcuQPZl4cTrBUshDhDh8aagrPaGAloA46hmBYihkwkp7eSpZzxSdS_qEhrhhaFhrhrhhacBrWahrhrBi5DUIAIHXBhrFB5qSi2sY-55ZoU"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iAmLywWHU-w280-h280/dell-inspiron-3520-i.webp",
        "productName": "Dell Inspiron 3520 IN3520P9K46002ORS1 Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹35,490",
        "rating": "4.2",
        "specScore": "55",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated UHD",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb58JU2dK~ed23z9ezNhrhAgTYBOr3Uh7iaTTcYuFBY3sucYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacZ4oPcUtYucTYWtUcTrBUshDhDh8aPAZGorg65X5ohmBYihkwkp7EdGX1b_7.vzEhrhhaFhrhrhhacBrWahrhrBi5yP3aATTahrFB5QIsBZjCXZfX8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i2EZmHNin-w280-h280/lenovo-v15-g4-laptop.webp",
        "productName": "Lenovo V15 G4 Laptop (AMD Athlon Silver 7120U/ 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹27,990",
        "rating": "4.6",
        "specScore": "44",
        "features": [
            "AMD Athlon Silver 7120U",
            "Dual Core, 2 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon 610M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqbR_pZwiVmlKDRhrhArnrysuhyihDRPwmGwpz_eh-hrhhaFhrhrhhacBrWahrhrBi5Y5n28tlOhrFB5RsdEr8Rn8ZF."
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i37bTySPH-w280-h280/hp-omen-16-xd0005ax.webp",
        "productName": "HP Omen 16-xd0005AX Gaming Laptop (AMD Ryzen 7 7840HS/ 16GB/ 1TB SSD/ Win11/ 6GB Graph)",
        "price": "₹1,09,900",
        "rating": "4.4",
        "specScore": "75",
        "features": [
            "7th Gen AMD Ryzen 7 7840HS",
            "Octa Core, 16 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 4050",
            "16.1 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJd_olN9.B8WTi_uDIhrhArnrysuhyihDRPwvbp7R_ph-hrhhaFhrhrhhacBrWahrhrBi5WZba8blThrFB5BvsvOvDC1qNo"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-igxJ15EPB-w280-h280/lenovo-s14-gen-3-82t.webp",
        "productName": "Lenovo S14 Gen 3 82TW000VIH Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ DOS)",
        "price": "₹52,990",
        "rating": "4.75",
        "specScore": "52",
        "features": [
            "12th Gen Intel Core i5 1235U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB DDR4  RAM",
            "512 GB SSD",
            "Intel UHD Graphics",
            "14 inches, 1920 x 1080 pixels",
            "DOS OS",
            "3 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwgBWqfp2_3ZEIZhrhArnrysuhyihDRPRe_d-ZG0h-hrhhaFhrhrhhacBrWahrhrBi58y5Uy84BhrFB5Y79Bjr5mxyI0"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iaoyLfOXa-w280-h280/acer-aspire-lite-15.webp",
        "productName": "Acer Aspire Lite 15 AL15-51 Laptop (AMD Ryzen 5 5500U/ 16GB/ 1TB SSD/ Win11)",
        "price": "₹38,849",
        "rating": "4.4",
        "specScore": "57",
        "features": [
            "5th Gen AMD Ryzen 5 5500U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "AMD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_RwJY2lFSamio6inhrhArnrysuhyihDRPwVmJpVf_h-hrhhaFhrhrhhacBrWahrhrBi5BF68Ot46hrFB5GIiR04Z8S5vS"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i1MyJAqxB-w280-h280/hp-victus-15-fa1098t.webp",
        "productName": "HP Victus 15-FA1098TX Laptop (12th Gen Core i5/ 8GB/ 512GB SSD/ Win11 Home/ 4GB Graph)",
        "price": "₹55,485",
        "rating": "4.65",
        "specScore": "60",
        "features": [
            "12th Gen Intel Core i5 12450H",
            "Octa Core (4P + 4E), 12 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_UqpnbDbf00AmFpmhrhArnrysuhyihDRPKlSmlGbHh-hrhhaFhrhrhhacBrWahrhrBi52INa3obthrFB5X0OYuCtolEyJ"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-it40ht1n4-w280-h280/dell-inspiron-7430-i.webp",
        "productName": "Dell Inspiron 7430 IC7430MH5K0M01ORS1 Laptop (13th Gen Core i5/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹80,390",
        "rating": "4.25",
        "specScore": "61",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "14 inches, 1920 x 1200 pixels, Touch Screen",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrEbqfTYKf_NQJXIhrhAgTYBOr3Uh7iaTTcYuFBY3sucYuUaTcAs3acY4c5ZUtcWauc5ZZ4CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnacGHZPcUtYucTYWtUcTrBUshDhDh8HXH6lbrAg4oirhmBYihkwkp7.pVxSe~1Sq-.hrhhaFhrhrhhacBrWahrhrBi588FBouDNhrFB5Vj8XUNqbyO2f"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iXtETnEvk-w280-h280/hp-victus-15-fb1002a.webp",
        "productName": "HP Victus 15-fb1002AX Gaming Laptop (AMD Ryzen 5 7535HS/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
        "price": "₹54,900",
        "rating": "4.4",
        "specScore": "65",
        "features": [
            "7th Gen AMD Ryzen 5 7535HS",
            "Hexa Core, 12 Threads",
            "8 GB DDR5 RAM",
            "512 GB SSD",
            "4 GB NVIDIA GeForce RTX 2050",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.a_Uqpz~i02i8xF-z3hrhArnrysuhyihDRPwweJ_VH1h-hrhhaFhrhrhhacBrWahrhrBi5OC5ZXDO8hrFB5e_X-pUt2OPkg"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iqXKq4bHX-w280-h280/hp-15s-er2004au-lapt.webp",
        "productName": "HP 15s-er2004AU Laptop (AMD Ryzen 7 5700U/ 16GB/ 512GB SSD/ Win11)",
        "price": "₹49,990",
        "rating": "4.75",
        "specScore": "54",
        "features": [
            "5th Gen AMD Ryzen 7  5700U",
            "Octa Core, 16 Threads",
            "16 GB DDR4 RAM",
            "512 GB SSD",
            "AMD Radeon",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDiK4JAPXPlTl9niiphrhAA3snrh7tBc54Fca3oPPHrCcrnic3Gc54cbcYuAtc5bW6c45oW6c8Yuis8FcnFcsggYAacoPo5crnic3riasucgCTTcticiYFBTrIcurUC3rTcFYThCclr5A5Brch-hDZPooGXhrhhaFhrhrhhacBrWahrhrBi5yoitPCObhrFB5F.Vmu7ziaFie"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iKZvIX3fa-w280-h280/hp-pavilion-plus-16.webp",
        "productName": "HP Pavilion Plus ‎16-ab0456TX Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win 11/ 6GB Graphics)",
        "price": "₹1,14,999",
        "rating": "4",
        "specScore": "72",
        "features": [
            "13th Gen Intel Core i7 13700H",
            "14 Cores (6P + 8E), 20 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "6 GB NVIDIA GeForce RTX 3050",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=125E6HIkXN7~x2nZBoDPtqRsUkhrhAgTYBOr3Uh7tBcBr2YTh3cBTCFcYuUaTcAs3acYGc5ZUtcWauc5ZGPPtc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacbcW6cW3rBtYAFcu2YiYrcWags3Aac3UDcZP4Pc5bcr6PH4bUDcWrnhNcTrBUshDhDh8a5ZgZXZi6Z4lGhmBYihkwkp70~ofvRv~H.KRhrhhaFhrhrhhacBrWahrhrBi53BtogN4yhrFB522A12lCeODqI"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iN5RyX8ql-w280-h280/dell-inspiron-3530-i.webp",
        "productName": "Dell Inspiron 3530 IN3530RMD8W001ORS1 Laptop (13th Gen Core i5/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹61,990",
        "rating": "4.05",
        "specScore": "50",
        "features": [
            "13th Gen Intel Core i5 1335U",
            "10 Cores (2P + 8E), 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnQrz2GjBE2e9gRoXqhrhAgTYBOr3Uh7iaTTcYuUaTcAs3acY4c5ZUtcWauc5ZZ4Cc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacYuFBY3sucZ4ZPcUtYucTYWtUcTrBUshDhDh8iaXHPGAbA46lihmBYihkwkp7z~_q1qZ.VSdXhrhhaFhrhrhhacBrWahrhrBi56Uat2g3ihrFB5zJtrmfgDY0G8"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imMdqEnYE-w280-h280/msi-vector-gp68-hx-1.webp",
        "productName": "MSI Vector GP68 HX 13VG-214IN Gaming Laptop (13th Gen Core i7/ 16GB/ 1TB SSD/ Win11/ 8GB Graph)",
        "price": "₹1,49,990",
        "rating": "4.5",
        "specScore": "77",
        "features": [
            "13th Gen Intel Core i7 13700HX",
            "16 Cores (8P + 8E), 24 Threads",
            "16 GB DDR5 RAM",
            "1 TB SSD",
            "8 GB NVIDIA GeForce RTX 4070",
            "16 inches, 2560 x 1600 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12-kEQTvRJpBmExoz_SANbap3lhrhArnrysuhyihDRPKX10lmdKh-hrhhaFhrhrhhacBrWahrhrBi5FHIrBHZohrFB5la2lwT_eKplF"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iFExzzC8L-w280-h280/asus-vivobook-15x-ol.webp",
        "productName": "Asus Vivobook 15X OLED M3504YA-LK552WS Laptop (AMD Ryzen 5 7530U/ 16GB/ 1TB SSD/ Win11 Home)",
        "price": "₹58,990",
        "rating": "4.1",
        "specScore": "61",
        "features": [
            "7th Gen AMD Ryzen 5 7530U",
            "Hexa Core, 12 Threads",
            "16 GB DDR4 RAM",
            "1 TB SSD",
            "Intel Iris Xe Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_IwbPnYFY7jS8RwKpVESH6hrhAgTYBOr3Uh7rFCFc2Y2s6ssOc54DcsTaicrnic3Iyauc4ctaDrcAs3acG4ZPCc5bcW6c5cU6cFFic8Yuis8Fc55ctsnacnZ4PHIrcTO44o8FcUtYucTYWtUcTrBUshDhDh84H5i6l65ia6GGhmBYihkwkp7ExKxp-x4dRRShrhhaFhrhrhhacBrWahrhrBi5yO2gbZaBhrFB50Ukt7eX8TIro"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iDycAM1Aj-w280-h280/lenovo-ideapad-3-15i.webp",
        "productName": "Lenovo IdeaPad 3 15IAU7 82RK00WXIN Laptop (12th Gen Core i3/ 8GB/ 256GB SSD/ Win11 Home)",
        "price": "₹33,999",
        "rating": "4.3",
        "specScore": "53",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "256 GB SSD",
            "Intel UHD Graphics",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GGlv~.afrynEsFIDSeAK_KwhrhArnrysuhyihDRPwvSXGleJh-hrhhaFhrhrhhacBrWahrhrBi5nIt3nbYDhrFB5uuEo~CQAOX1d"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-icDhrRu8A-w280-h280/lenovo-ideapad-1-15a.webp",
        "productName": "Lenovo IdeaPad 1 15AMN7 82VG00ERIN Laptop (AMD Ryzen 3 7320U / 8GB/ 512GB SSD/ Win11 Home)",
        "price": "₹31,890",
        "rating": "4.25",
        "specScore": "51",
        "features": [
            "7th Gen AMD Ryzen 3 7320U",
            "Quad Core, 8 Threads",
            "8 GB LPDDR5 RAM",
            "512 GB SSD",
            "AMD Radeon 610M",
            "15.6 inches, 1920 x 1080 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12GbaP3eDi2Gos2bUWoE50CGPhrhAA3snrh7Taus2scYiarBric5c54rnuGcrnic3IyaucZc54cbcYuAtcXW6c45oW6c8Yuis8Fc55ctsnacnFcsggYAacoPo5crnic3riasucgticiYFBTrIcATsCicW3aIcXo2WPPa3Yuch-hDZP5HoXhrhhaFhrhrhhacBrWahrhrBi5FADBuiiThrFB5JON.NqYTVP1T"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i8d8BbDnr-w280-h280/hp-250-g9-7m657pa-la.webp",
        "productName": "HP 250 G9 7M657PA Laptop (12th Gen Core i3/ 8GB/ 512GB SSD/ Win11)",
        "price": "₹32,490",
        "rating": "4.4",
        "specScore": "56",
        "features": [
            "12th Gen Intel Core i3 1215U",
            "Hexa Core (2P + 4E), 8 Threads",
            "8 GB DDR4 RAM",
            "512 GB SSD",
            "Intel Integrated",
            "15.6 inches, 1366 x 768 pixels",
            "Windows 11 OS",
            "1 Year Warranty"
        ],
        "actions": {
            "compareButton": "Compare",
            "likeButton": "Like",
            "buyLink": "https://l.smartprix.com/l?k=12_Iwbb52sFqxF~6DK1~gIWAhrhAgTYBOr3Uh7tBco4PcWlcYuUaTcAs3acYZc5oUtcWauc5o54CcXcW6c45ocW6cFFic8Yuis8Fc55ctsnac6CFYuaFFcTrBUshDhDh8rar6ZaGPAHb4ihmBYihkwkp7JfJKG7zx7x~ShrhhaFhrhrhhacBrWahrhrBi5ZNQGo8GZhrFB55sWsGglkbPd~"
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJd2TTEJp-w280-h280/hp-victus-15-fa1351t.webp",
        "productName": "",
        "price": "₹57,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-imCxSargW-w280-h280/asus-vivobook-15-x15.webp",
        "productName": "",
        "price": "₹51,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-i3lWoUzaO-w280-h280/acer-aspire-7-a715-7.webp",
        "productName": "",
        "price": "₹53,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ieUw4VMBj-w280-h280/asus-vivobook-16x-k3.webp",
        "productName": "",
        "price": "₹74,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iLH4fh4Iu-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "",
        "price": "₹52,890",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-ifHKwQY9N-w280-h280/acer-swift-go-14-sfg.webp",
        "productName": "",
        "price": "₹56,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iuyE8KL7Z-w280-h280/lenovo-ideapad-slim.webp",
        "productName": "",
        "price": "₹63,990",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    },
    {
        "imageUrl": "https://cdn1.smartprix.com/rx-iJavk42Bg-w280-h280/hp-victus-15-fb0150a.webp",
        "productName": "",
        "price": "₹53,999",
        "rating": "N/A",
        "specScore": "",
        "features": [],
        "actions": {
            "compareButton": "",
            "likeButton": ""
        }
    }
]




df = pd.DataFrame(data)

pdb.set_trace()