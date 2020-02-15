#include "if_curr_CODE/definitions.h"

#include <iostream>

// GeNN userproject includes
#include "spikeRecorder.h"
#include "timer.h"

int main()
{
    try
    {
        allocateMem();
        initialize();
        initializeSparse();

        // Loop through timesteps
        while (t < 1000.0) {
            stepTime();
        }

        std::cout << neuronUpdateTime << "ms" << std::endl;
    }
    catch (std::exception &e)
    {
        std::cerr << e.what() << std::endl;
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
