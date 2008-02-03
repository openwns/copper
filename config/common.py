import os
import CNBuildSupport
from CNBuildSupport import CNBSEnvironment
import wnsbase.RCS as RCS

commonEnv = CNBSEnvironment(PROJNAME       = 'Copper',
                            PROJMODULES    = ['TEST', 'BASE'],
                            FLATINCLUDES   = False,
                            LIBRARY        = True,
                            SHORTCUTS      = True,
                            DEFAULTVERSION = True,
			    REVISIONCONTROL = RCS.Bazaar('../', 'Copper', 'main', '1.0'),
                            )
Return('commonEnv')

