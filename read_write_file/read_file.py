def read_file(file_name,list_out):
    open_file = 'input_files/' + file_name
    print('Open file :', file_name)
    # membaca isi teks
    with open(open_file, newline='') as txtfile:
        # memetakan isi teks ke dalam list
        all_text = []
        for line in txtfile:
            all_text.append(line.strip()
    print('Open file :', file_name + ' [DONE]')
    # menentukan batas awal dan akhir
    for i,j in enumerate(all_text):
        for k,m in enumerate(all_text[i]):
            start_keyword = reduce(operator.getitem, [i,k], all_text)
            if start_keyword == '__start__':
                start_row = i+2
                print('Start Row :', start_row)
            stop_keyword = '__stop__'
            if any(stop_keyword in m for s in all_text):
                stop_row = i-2
                print('Stop Row  :', stop_row)
    # memilih teks yang diperlukan
    selected_text = []
    for i in all_text[start_row:stop_row+1]:
        selected_text.append(i)
    # salin isi dari selected_text ke list_out
    for i in selected_text:
        list_out.append(i)
    return list_out
