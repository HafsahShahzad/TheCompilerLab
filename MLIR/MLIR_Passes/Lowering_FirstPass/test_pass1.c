float add_zero(float x) {
    float y = x + 0.0f;   // This should be simplified by the pass
    return y;
}

float add_nonzero(float x) {
    float y = x + 1.0f;   // This should NOT be simplified
    return y;
}
