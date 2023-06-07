#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;

vec3 pallete( float t) {
    vec3 a = vec3(0.706 ,0.161, 0.732);
    vec3 b = vec3(0.179 ,0.198 ,0.020);
    vec3 c = vec3(0.187 ,0.713 ,0.196);
    vec3 d = vec3(4.086 ,2.624 ,3.019);

    return a + b*cos(6.28318*(c*t*d));
}

void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy)/ u_resolution.xy;
    vec2 uvo = uv;
    vec3 fincol = vec3(0.0);

    for(float i=0.0; i <4.; i++){

        uv = fract(uv*2.) - 0.5;

        float d = length(uv) * exp(-length(uvo));

        vec3 col = pallete(length(uvo) + i*4. + u_time/4.);

        d = sin(d*8. + u_time)/8.;
        d = abs(d);

        d = 0.02/d;

        fincol += col * d;
    }

    gl_FragColor = vec4(fincol,1.0);
}