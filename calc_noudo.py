def calc_bunryou(moto_noudo, req_noudo, youryou):
    temp_bairitu = moto_noudo / req_noudo
    input_youryou = youryou / (temp_bairitu + 1)
    return input_youryou

if __name__ == '__main__':
    print('Input : ' , (calc_bunryou(500, 50, 500)) , 'ml')
    
