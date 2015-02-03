# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from unittest.mock import patch, MagicMock
from uuid import uuid4

from gns3.project import Project


def test_project_create():

    uuid = uuid4()
    mock = MagicMock
    with patch("gns3.http_client.HTTPClient.post") as mock:

        signal = MagicMock()

        project = Project()
        project.project_created_signal.connect(signal)
        project.create()

        args, kwargs = mock.call_args

        assert args[0] == "/project"
        assert kwargs["body"] == {"temporary": False, "uuid": None}
        # Call the project creation callback
        args[1]({"uuid": uuid})
        assert project.uuid() == uuid

        assert signal.called


def test_project_close():

    uuid = uuid4()
    mock = MagicMock
    with patch("gns3.http_client.HTTPClient.post") as mock:

        signal = MagicMock()

        project = Project()
        project.setUuid(uuid)

        mock_signal = MagicMock()
        mock_signal_closed = MagicMock()
        project.project_about_to_close_signal.connect(mock_signal)
        project.project_closed_signal.connect(mock_signal_closed)

        project.close()

        assert mock_signal.called
        assert not mock_signal_closed.called

        args, kwargs = mock.call_args

        assert args[0] == "/project/{uuid}/close".format(uuid=uuid)
        assert kwargs["body"] == {}

        # Call the project close callback
        args[1]({"uuid": uuid})
        assert mock_signal_closed.called

        assert project.closed()