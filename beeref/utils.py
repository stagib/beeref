# This file is part of BeeRef.
#
# BeeRef is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BeeRef is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BeeRef.  If not, see <https://www.gnu.org/licenses/>.


from PyQt6 import QtCore


def get_rect_from_points(point1, point2):
    """Constructs a QRectF from the given QPointF. The points can be *any*
    two opposing corners of the rectangle."""

    topleft = QtCore.QPointF(
        min(point1.x(), point2.x()),
        min(point1.y(), point2.y()))
    bottomright = QtCore.QPointF(
        max(point1.x(), point2.x()),
        max(point1.y(), point2.y()))
    return QtCore.QRectF(topleft, bottomright)
