#version 330

uniform sampler2D Texture;
in vec2 uvs;
out vec4 FragColor;

uniform float uTime;
float wind_strength = 2.0;

void main() {
    float distort = (sin(uTime/2)*(1.0-uvs.y))/96;
    vec2 distortedUV = vec2(uvs.x + distort * wind_strength, uvs.y);
    vec4 texColor = texture(Texture, distortedUV);
    FragColor = texColor;
}
