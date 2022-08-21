"""Run analyses across sessions."""

from convnwb.io import get_files, save_json, load_nwbfile, file_in_list
from convnwb.utils import print_status

# Import settings from local file
from settings import RUN, PATHS

# Import local code
import sys
sys.path.append('../code')
from reports import xx

###################################################################################################
###################################################################################################

def main():
    """Run session analyses."""

    print_status(RUN['VERBOSE'], '\n\nRUNNING SESSION ANALYSES - {}\n\n'.format(RUN['TASK']), 0)

    nwbfiles = get_files(PATHS['DATA'], select='nwb')

    for nwbfile in nwbfiles:

        ## LOADING & DATA ACCESSING

        # Check and ignore files set to ignore
        if file_in_list(nwbfilename, RUN['IGNORE']):
            print_status(RUN['VERBOSE'], 'Skipping file (set to ignore): {}'.format(nwbfilename), 0)
            continue

        # Load file and prepare data
        print_status(RUN['VERBOSE'], 'Running session analysis: {}'.format(nwbfilename), 0)

        # Load NWB file
        nwbfile, io = load_nwbfile(nwbfilename, PATHS['DATA'], return_io=True)

        ## EXTRACT DATA OF INTEREST
        ...

        ## PRECOMPUTE MEASURES OF INTEREST
        ...

        ## CREATE SESSION REPORT
        ...

        # Save out the report
        save_figure('session_report_' + subject_info['session_id'] + '.pdf',
                    PATHS['REPORTS'] / 'session', close=True)

        # Close the nwbfile
        io.close()

    print_status(RUN['VERBOSE'], '\n\nCOMPLETED SESSION ANALYSES\n\n', 0)

if __name__ == '__main__':
    main()
