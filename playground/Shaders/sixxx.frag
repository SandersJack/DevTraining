#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;

vec3 pallete( float t) {
    vec3 a = vec3(0.706 ,0.161, 0.732);
    vec3 b = vec3(0.301 ,0.933 ,0.874);
    vec3 c = vec3(0.776 ,0.731 ,0.822);
    vec3 d = vec3(5.274 ,6.096 ,3.701);

    return a + b*cos(6.28318*(c*t*d));
}

void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy)/ u_resolution.xy;
    vec2 uvo = uv;
    vec3 fincol = vec3(0.0);

    for(float i=0.0; i <4.; i++){

        uv = fract(uv*1.3) - 0.5;

        float d = length(uv) * exp(-length(uvo));

        vec3 col = pallete(length(uvo) + i*4. + u_time/4.);

        d = sin(d*8. + u_time)/8.;
        d = abs(d);

        d = pow(0.01/d,1.);

        fincol += col * d;
    }

    gl_FragColor = vec4(fincol,1.0);
}