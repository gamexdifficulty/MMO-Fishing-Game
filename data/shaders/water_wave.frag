#version 330

in vec2 uvs;
out vec4 FragColor;

uniform float uTime;

float amplitude = 0.125;

void main() {
    vec3 waterColor = vec3(0.227, 0.369, 0.753);

    float wave1 = sin(uvs.x * 40.0 + uTime * 1.5);
    float wave2 = sin(uvs.x * 70.0 + uTime * 1.1);
    float wave3 = cos(uvs.x * 100.0 + uTime * 0.8);

    float combined = (wave1 * 0.6 + wave2 * 0.3 + wave3 * 0.2) / 1.1;
    float waveY = 0.25 + combined * amplitude;

    if (uvs.y > waveY) {
        FragColor = vec4(waterColor, 1.0);
    } else {
        FragColor = vec4(0.0, 0.0, 0.0, 0.0);
    }
}
