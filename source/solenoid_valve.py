'''
Copyright 2024-2025, the Active Cooling Experimental Application Authors

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import numpy as np

class Solenoid:

    def __init__(self, n_region, test_UI = False):

        self.test_UI = test_UI
        self.state = np.zeros(n_region)
        self.state = self.state.astype(bool)

        if test_UI:
            return

        import board
        import RPi.GPIO as GPIO
        from source.DRV8806 import DRV8806

        self.DRV = [DRV8806(0, 0), DRV8806(0, 1), DRV8806(10, 0)]
    
    def set_solenoid(self, solenoid_number, on=False):
        if 0 <= solenoid_number <= 3:
            self.DRV[0].set_output(solenoid_number, on)
        elif 4 <= solenoid_number <= 7:
            self.DRV[1].set_output(solenoid_number - 4, on)
        elif 8 <= solenoid_number <= 11:
            self.DRV[2].set_output(solenoid_number - 8, on)
        else:
            raise ValueError("Solenoid number must be between 0 and 11")


