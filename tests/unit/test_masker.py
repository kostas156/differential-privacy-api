from app.core.pii.masker import masker

def test_mask_email():
    result = masker.mask("Contact us at test@example.com")
    assert "[EMAIL_ADDRESS]" in result["masked_text"]
    assert "test@example.com" not in result["masked_text"]

def test_mask_person():
    result = masker.mask("My name is John Doe.")
    assert "John Doe" not in result["masked_text"]

def test_mask_detection_count():
    result = masker.mask("Email: test@example.com. Phone: +1 555 123 4567.")
    assert result["detection_count"] >= 1

def test_mask_no_pii():
    result = masker.mask("The weather is nice today.")
    assert "test@example.com" not in result["masked_text"]
    assert "John" not in result["masked_text"]

def test_mask_specific_entities():
    result = masker.mask(
        text="Call John at john@example.com",
        entities=["EMAIL_ADDRESS"]
    )
    assert "[EMAIL_ADDRESS]" in result["masked_text"]
    assert result["detection_count"] == 1