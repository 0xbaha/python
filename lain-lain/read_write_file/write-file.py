def write_file(list_in,name):
    date_generated = strftime("%y%m%d%H%M", localtime())
    file_name = 'rule_' + date_generated + '.py'
    cmd_text = 'Write file: ' + file_name
    print(cmd_text)
    dir_file = 'output_files/' + file_name
    with open(dir_file, 'a') as f:
        f.write("# Feature name: %s\n" % name)
        f.write("def check_%s(%s):\n" % (name,name))
        for i in list_in:
            f.write("\t%s\n" % i)
        f.write("\n")
    print(cmd_text + ' [DONE]')
    return
