import os
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/kpay_detect')))
from kpay_processor import KPaySlipProcessor

def test_kpay_slip_processor_with_valid_image():
    # Arrange
    test_image = "kpay.jpg"
    test_image_path = os.path.join("src\\kpay_detect\\data", test_image)
    if not os.path.exists(test_image_path):
        pytest.skip(f"Test image {test_image_path} not found.")
    processor = KPaySlipProcessor(test_image_path)

    # Act
    result = processor.process()

    # Assert
    assert result is not None, "No data extracted from slip."
    assert "clean_amount" in result
    assert "name" in result
    assert "phone" in result
    assert isinstance(result["clean_amount"], int)
    assert isinstance(result["name"], str)
    assert isinstance(result["phone"], str)


if __name__ == "__main__":
    pytest.main([__file__])