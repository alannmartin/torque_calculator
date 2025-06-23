# window.py
#
# Copyright 2025 alan martin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk

@Gtk.Template(resource_path='/com/github/alannmartin/torque_calculator/notebook.ui')
class TorqueCalculatorWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'TorqueCalculatorWindow'

    #child xml elements

    notebook = Gtk.Template.Child()
    btnOne = Gtk.Template.Child()
    entry1 = Gtk.Template.Child()
    lblMass = Gtk.Template.Child()
    lblDrum = Gtk.Template.Child()
    lblRadGyration = Gtk.Template.Child()
    lblLinearAccel = Gtk.Template.Child()
    lblAngAccel1 = Gtk.Template.Child()
    lblHeading = Gtk.Template.Child()
    lblTorque1 = Gtk.Template.Child()
    entry2 = Gtk.Template.Child()
    entry3 = Gtk.Template.Child()
    entry4 = Gtk.Template.Child()
    lblAngAccel2 = Gtk.Template.Child()
    lblmoi = Gtk.Template.Child()
    lblTorque2 = Gtk.Template.Child()
    lblMOIHoistDrum = Gtk.Template.Child()
    lblTorqueFormula = Gtk.Template.Child()
    lblFormulaAlpha = Gtk.Template.Child()
    lblFormulaMass = Gtk.Template.Child()
    lblFormulaRadGyration = Gtk.Template.Child()
    lblMessage = Gtk.Template.Child()

    # child signal element in notebook.ui
    @Gtk.Template.Callback()
    def calculate(self, btnOne):
        #self.lblMessage.set_label('It works..')

        # Store input values in a unique variable
        mass  = self.entry1.get_text()
        rDrum = self.entry2.get_text()
        rGyr  = self.entry3.get_text()
        accel = self.entry4.get_text()

        #validate the inputs and convert strings to a float
        if ((accel != '')  and  (rDrum != '' ) and (rGyr != '') and (accel != '')):
            torque = float(mass) * float(rGyr) * float(rGyr) * float(accel)/float(rDrum)

            #show the calculated torque
            self.lblTorque2.set_text(str(torque)+" Nm")

            #show the calculated moi
            moi = float(mass) * float(rGyr) * float(rGyr)
            self.lblmoi.set_text(str(moi) + " kg.m\u00B2")

            #show the calculated angular acceleration
            alpha = float(accel) / float(rDrum)
            self.lblAngAccel2.set_text(str(alpha)+" rad/sec\u00B2")

            self.lblMessage.set_text(" ")

             #show the user an error message because the inputs are empty
        else:
            self.lblMessage.set_text("Please enter ALL values")




    def __init__(self, **kwargs):
        super().__init__(**kwargs)
