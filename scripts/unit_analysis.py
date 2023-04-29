"""Run analyses across units."""

from convnwb.io import load_nwbfile, get_files, save_json, file_in_list
from convnwb.utils.log import print_status
from convnwb.utils.run import catch_error

# Import settings from local file
from settings import RUN, PATHS, UNITS, XX

# Import local code
import sys
sys.path.append('../code')
from reports import XX

###################################################################################################
###################################################################################################

def main():
    """Run unit analyses."""

    print_status(RUN['VERBOSE'], '\n\nANALYZING UNIT DATA - {}\n\n'.format(RUN['TASK']), 0)

    # Get the list of NWB files
    nwbfiles = get_files(PATHS['DATA'], select='nwb')

    # Get list of already generated and failed units, & drop file names
    output_files = get_files(PATHS['RESULTS'] / 'units'
                             select='json', drop_extensions=True)
    failed_files = get_files(PATHS['RESULTS'] / 'units' / 'zFailed',
                             select='json', drop_extensions=True)

    for nwbfilename in nwbfiles:

        ## DATA LOADING

        # Check and ignore files set to ignore
        if nwbfilename.split('.')[0] in RUN['IGNORE']:
            print_status(RUN['VERBOSE'], '\nSkipping file (set to ignore): {}'.format(nwbfilename), 0)
            continue

        # Print out status
        print_status(RUN['VERBOSE'], '\nRunning unit analysis: {}'.format(nwbfilename), 0)

        # Load NWB file
        nwbfile, io = load_nwbfile(nwbfilename, PATHS['DATA'], return_io=True)

        ## GET DATA
        ...

        ## ANALYZE UNITS

        # Get unit information
        n_units = len(nwbfile.units)

        # Loop across all units
        for unit_ind in range(n_units):

            # Initialize output unit file name & output dictionary
            name = session_id + '_U' + str(unit_ind).zfill(2)
            results = {}

            # Check if unit already run
            if UNITS['SKIP_ALREADY_RUN'] and name in output_files:
                print_status(RUN['VERBOSE'], 'skipping unit (already run): \tU{:02d}'.format(unit_ind), 1)
                continue

            if UNITS['SKIP_FAILED'] and name in failed_files:
                print_status(RUN['VERBOSE'], 'skipping unit (failed): \tU{:02d}'.format(unit_ind), 1)
                continue

            print_status(RUN['VERBOSE'], 'running unit: \t\t\tU{:02d}'.format(unit_ind), 1)

            # Extract spikes for a unit of interest
            spikes = nwbfile.units.get_unit_spike_times(unit_ind)

            try:

                ## Compute measures
                ...

                ## Collect results
                ...

                # Save out unit results
                save_json(results, name + '.json', folder=str(PATHS['RESULTS'] / 'units'))

            except Exception as excp:

                catch_error(UNITS['CONTINUE_ON_FAIL'], name, PATHS['RESULTS'] / 'units' / 'zFailed',
                            RUN['VERBOSE'], 'issue running unit #: \t{}')

    print_status(RUN['VERBOSE'] '\n\nCOMPLETED UNIT ANALYSES\n\n', 0)

if __name__ == '__main__':
    main()
