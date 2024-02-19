import logging
from typing import Any, Dict

import pytest
from infra.adapters.storage.minio_adapter import MinioAdapter

from tests.utils.base_tests import BaseUnitTest


class TestMinioAdapter(BaseUnitTest):
    def test_should_return_an_typeerror_if_no_init_arg_is_informed(self) -> None:
        with pytest.raises(expected_exception=TypeError) as exec_info:
            sut = MinioAdapter(logger=logging.Logger)
            assert sut is None
            assert exec_info.type is TypeError
            assert exec_info.value.args[0] == str(
                "__init__() missing 4 required positional arguments: 'host', 'access_key', 'secret_key', and 'secure'"
            )

    def _get_dummy_connection(self) -> Dict[Any, Any]:
        return dict(
            logger=logging.Logger,
            host="localhost",
            access_key="fake-access-key",
            secret_key="fake-secret-key",
            secure=False,
        )

    def test_should_return_an_instance_of_mionio_adapter(self) -> None:
        # Arrange
        _config = self._get_dummy_connection()
        # Act
        sut = MinioAdapter(**_config)
        # Assert
        assert isinstance(sut, MinioAdapter)
