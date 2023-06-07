#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;

vec3 pallete( float t) {
    vec3 a = vec3(0.834, 0.665 ,0.963);
    vec3 b = vec3(0.907 ,0.402 ,0.208);
    vec3 c = vec3(0.879 ,1.021 ,1.367);
    vec3 d = vec3(2.972 ,2.147 ,5.386);

    return a + b*cos(6.28318*(c*t*d));
}

void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy)/ u_resolution.xy;
    vec2 uvo = uv;

    uv = fract(uv*2.) - 0.5;

    float d = length(uv);

    vec3 col = pallete(length(uvo) + u_time/5.);

    d = sin(d*8. + u_time)/8.;
    d = abs(d);

    d = (0. - abs(sin(u_time/100.)))/d;

    col *= d;

    gl_FragColor = vec4(col,1.0);
}