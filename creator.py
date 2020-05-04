import create_options
import staff
import misc_helpers

def main():
    options = create_options.get_options()
    misc_helpers.delete_and_create_folder(options["output_folder_complete"])
    staffs = staff.get_staffs(options["lily_file"])
    misc_helpers.write_debug_file(staffs, options["output_folder_complete"])



if __name__ == '__main__':
    main()
