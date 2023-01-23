from pyzandro.masterserver import parse_packet
from pyzandro.masterserver import MSC_ENDSERVERLISTPART
from pyzandro.masterserver import MSC_ENDSERVERLIST


def test_parse():
    p1 = b'\xff\x06\x00\x00\x00\x00\x08\x01d\x0b\xf0W\xa5\x13\x01d\x0fq\xb7\xaa)\x03g\x19;\x1b\xab)\xac)\xad)\x0fh\x80:x\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xb6)\xb7)\xb8)\x01h\xec\xa0\x9f\xaa)\x01\x82=V3\xaa)\x01\x85\xa7L\x0b\xaa)\x1e\x86\xc3\x0e\x88\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\xb3)\xb5)\xb6)\xb7)\xb8)\xb9)\xba)\xbb)\xbc)\xbd)\xbe)\xbf)\xc0)\xc1)\xc2)\xc3)\xc4)\xc6)\xc7)\xc8)\xc9)\xca)\x02\x8a\xc7\x12\x9a\xaa)\xab)#\x8e\x84\x9b\xa3\xab)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xb6)\xb7)\xb8)\xb9)\xba)\xbb)\xbc)\xbd)\xbe)\xbf)\xc0)\xc1)\xc2)\xc3)\xc4)\xc5)\xc6)\xc7)\xc9)\xca)\xcb)\xcc)\xcd)\xce)\xcf)\xd0)\xd1)\x05\x90\xca;)P\xd3$\xdcL\xe6U\xf3T\xfd\x01\x92;\xcbP\xaa)\x01\x93\x87\x99\x14\xaa)\x01\x93\xb6\xffI\xaa)\x01\x98%T\x11\x8c\x16\n\x98C.\x1b\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xbaP\xbbP\xbcP\x02\x99`0\x0f\xbe\x9es\x1c\x01\x9a5)\xc7\xaa)\x05\x9b\xf8\xc6v\xc2%\xc3%\xc4%\xc5%\xc6%\x04\x9f\xc4\x80?\xbc\x0b\xbd\x0b\xbe\x0b\xbf\x0b\x02\xa2\xd4\x9eW\xab)\xac)\x01\xa2\xf8^y\xaa)\t\xa2\xf8_I\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\x02\xa7\xeb=\xd1\xaa)j\r\x04\xb2v\x9fC\xac)\xad)\xae)\xaf)\x04\xb2Y\xf5\x08\xa9)\xaa)\xab)\xac)\x01\x12\xe0\xb3\xa2\xaa)\x01\xb7\xc5+\x8f\x12*\x0f\xb9\x96\xbd8\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xcc)\xcd)\xcf)\x01\xb9\xfa\xd4\xd6\xe4\xad\x01\xba\x1f\n+\x01\x04\x01\xbc\x8f(\xac\xaa)\x01\xbe\x16\'\x17\xaa)\x03\xbe\xf5\x83b\xaa)\xc2)\x94*\x17\xc0\x9bZY\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xb6)\xb7)\xb8)\xb9)\xba)\xbb)\xbc)\xbd)\xbe)\xbf)\xc0)\x01\xc0E\xb5\xbe\xab)\x04\xc2\x84\xa4\xf5\xaa)\xab)\xac)\xad)\x01\xc9_\xaf\x93\xaa)\x05\xd5\x12\x8f\x17\xb1)\xb2)\xb3)\xb4)\xb5)\x01\xd5 \x07V\xaa)\x01\xd9\x1b\xe2\x8a\xaa)\x01\xd9O\xbdo\xaa)\x06\x17l98\xaa)\xab)\xac)\xad)\xae)\xb0)\n\x17\xe9\x104\xaa)\xad)\xae)\xb2)\xb7)\xb8)\xe2>\x90r\xd2\xb1\x82\xc9\x05\x03\x12\x8d\xba\xa5)\xa6)\xa7)\xa8)\xaa)\x01\x03\xdf\x04\xe7\xaa)\r%\x99\x01,\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb2)\xb5)\xb6)\xb7)\xb8)\x01\'eD\x08\xca)\x02+\xf8\xb8\xf8\xa8\x0c\xa9\x0c\x12-\x8d\x80\xd2N)\xa8)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xb6)\xb7)\xb9)\xba)\xbb)\xbc)\xbe)\x18*\x1f*\x01-\x02\xc0\x14\xaa)\x01-\x1a\xe3\xc5"Y\x01- \xd4p\xaa)\x06-8\\\x8b\xaa)\xab)\xac)\xad)\xae)\xaf)\x01-O\xca\xe5\xaa)\x03.$)\xf1\xaa)\xab)\xac)\x01/\xbd\xaf\xd1\xab)\x01/\xd3\xc0\x05IW\x05\x05\'X\x03BdCdDdEdFd\x022t\x14o\xac)\xad)\x023\xc3t~\xaa)\xab)\x013\xc3\xbda\xaa)\x023\xd2\x05\xf2\xcd)\xce)\x016\xe8\xd3\x19\xaa)\x136$\xa5\xa7\xab)\xad)\xaf)\xb0)\xb1)\xb2)\xb3)\xb4)\xb5)\xb6)\xb7)\xb8)\xb9)\xba)\xbb)\xbc)\xbf)\xc0)\xd1)\x01>m\x07M\xab)\x04@Ja\xb1\xaa)\xab)\xac)\xcc)\x02@bW\n\xaa)\x92-\x01A\x1e=5\xc9)\x01CG\x9f\xf9\xaa)\x01D\x81\xde\x11\xaa)\x08D\xc5\xb0\x96\xaf)\xb1)\xb3)\xb4)\xb5)\xb6)\xb7)\xba)\x00\x07'
    p2 = b"\xff\x06\x00\x00\x00\x01\x08\x02D\x03\xf1\xa8\xa8)\xab)\x0fE\xc3\x80\xeaQ-R-S-T-U-V-W-X-Y-Z-[-\\-]-^-_-\x04E.:\xb4\xaf)\xb0)\xb1)\xb2)\x01F\xbeh\r\xaa)\x02G\xa4q\xd1\xaa)\xab)\x06G\x1b\x89\xd9\xaa)\xab)\xac)\xad)\xae)\xaf)\x02H\xd1/\xbf\xaa)\xab)\x01I\xb0\xb80\xad)\x01J[}\x9a\xa4)\x07J[~\xc6\xaa)\xac)\xfe)\x17*0*1*\x88*\x01M\xfc/\xd0\x85\xc6\x01N(\xd9^\xaa)\x01N<\x8e\x85\xaa)\x1cO\xae\x0f\x8c\xe9)\xea)\xeb)\xec)\xed)\xee)\xef)\xf0)\xf1)\xf2)\xf3)\xf4)\xf5)\xf6)\xf7)\xf8)\xf9)\xfa)\xfb)\xfc)\xfd)\xfe)\xff)\x00*\x01*\x02*\x03*\x04*\nO\xcfr=\xa4)\xa5)\xa6)\xa7)\xa8)\xa9)\xaa)\xab)\xac)\xad)\x01PRvE\xaa)\x01Q\xd1\x92m\x88*\x01R\xd1\xd1\xa4\xaa)\x06R\xdf\x03\x87\xaa)\xab)\xac)\xad)\xae)\xaf)\x02RB=\x9e\xaa)\xab)\x01RE\x02\xfa]\xab\x01T\xd8\x8d\xc0\xaa)\x01U\xdd\x11\xa6\xaa)\x01V\x83\xd13\xaa)\x01V\x08\x05*^m\x01Y\xf7\xff\xe9\x08d\x04Ze\xb6\x8d\x1e\x9a\xba\xb2\x86\xb5\x13\xcf\x01[BZ+\xaa)\x05\\\xcd\x1a\x12\x9a)\xa4)\xa8)\xaa)\xac)\n\\\xcd\x1f\xdf\xae)\xb0)\xb2)\xb4)\xb6)\xb8)\xba)\xbc)\xbe)\xc0)\x01]\xdf2L\xaa)\x05^\xad\xa4\xac\xac)\xad)\xb0)\xb9)\xba)\x02^\xfe>\xa3pdsd\x01^\xff\x8f\t\xaa)\x02_\xa5\x8a\x08\x012\x022\x01_1\x9a\xdd\xaa)\naq\x1f\x95\xaa)\xab)\xac)\xad)\xae)\xaf)\xb0)\xb1)\xb3)\xb4)\x01c\x01)v\xaa)\x01ci\xec\xad\xac)\x01c'y\x89\xaa)\x00\x02"
    r = {}
    parse_packet(p1, r)
    assert r['closing_status'] == MSC_ENDSERVERLISTPART
    assert len(r['ip_list']) == 325
    parse_packet(p2, r)
    assert len(r['ip_list']) == 469
    assert r['closing_status'] == MSC_ENDSERVERLIST

    
    