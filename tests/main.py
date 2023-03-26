from tests.tags import *

start_dir = '../app'
html_files = find_html_files(start_dir)
check_i18n_attributes(html_files)