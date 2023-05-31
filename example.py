from distributor import Client


if __name__ == '__main__':
    file_list = glob.glob('files_to_be_processed/*')


    client = Client(file_list)
    while True:
        if client.alive():
            i = client.get_job()
            processs_parquet(i, kenlm_model_en, kenlm_model_books)
            client.complete_job(i)
        else:
            break