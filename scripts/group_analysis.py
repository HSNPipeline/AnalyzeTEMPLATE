"""Run analyses across the group."""

from hsntools.io import get_files, file_in_list
from hsntools.run import print_status

# Import settings from local file
from settings import RUN, PATHS

# Import local code functions
import sys
sys.path.append('../code')
from reports import XX

###################################################################################################
###################################################################################################

def main():
    """Run group level summary analyses."""

    print_status(RUN['VERBOSE'], '\n\nANALYZING GROUP DATA \n\n', 0)

    # Get the list of NWB files
    nwbfiles = get_files(PATHS['DATA'])

    ## COLLECT INFORMATION

    # Define summary data to collect
    summary = {
        'ids' : [],
        'n_trials' : [],
        'n_units' : [],
        ...
    }

    for nwbfilename in nwbfiles:

        ## LOADING & DATA ACCESSING

        # Check and ignore files set to ignore
        if file_in_list(nwbfilename, RUN['IGNORE']):
            print_status(RUN['VERBOSE'], 'Skipping file (set to ignore): {}'.format(nwbfilename), 0)
            continue

        # Load NWB file
        nwbfile, io = load_nwbfile(nwbfilename, PATHS['DATA'], return_io=True)

        # Collect information across the group
        summary['ids'].append(nwbfile.session_id)
        summary['n_units'].append(len(nwbfile.units))
        summary['n_trials'].append(len(nwbfile.trials))
        ...

        # Close the nwbfile
        io.close()

    # Collect information of interest
    group_info = create_group_info(summary)

    ## CREATE REPORT

    # Save out report
    save_figure('group_report.pdf', PATHS['REPORTS'] / 'group', close=True)

    print_status(RUN['VERBOSE'], '\n\nCOMPLETED GROUP ANALYSES\n\n', 0)

if __name__ == '__main__':
    main()
