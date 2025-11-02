#version 330

uniform sampler2D Texture;
in vec2 uvs;
out vec4 FragColor;

uniform float uTime;

void main() {
    float waveStrength = 0.075;
    float waveFrequency = 75.0;
    float waveSpeed = 0.75;
    vec3 waterFillColor = vec3(0.227, 0.369, 0.753);

    float x = uTime;

    float waveX = 0.5;
    // float waveX = sin(uvs.y * waveFrequency + uTime * waveSpeed);
    float waveY = 1.0;
    // if (uvs.y <= 0.5) {
        // waveY = );
        // waveY = cos(uvs.x * waveFrequency * 0.8 + uTime * waveSpeed * 1.2);
    // }

    vec2 distortedUV = uvs + vec2(waveX, waveY) * waveStrength;
    
    vec4 texColor = vec4(0.0);
    if (distortedUV.y >= 0.0 && distortedUV.y <= 1.0) {
        distortedUV = clamp(distortedUV, 0.0, 1.0);
        texColor = texture(Texture, distortedUV);
    } else {
        texColor = vec4(waterFillColor, 1.0);
    }

    FragColor = texColor;
}
