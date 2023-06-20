#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;

vec3 pallete( float t) {
    vec3 a = vec3(0.854 ,0.414 ,0.217);
    vec3 b = vec3(0.179 ,0.198 ,0.020);
    vec3 c = vec3(0.187 ,0.713 ,0.196);
    vec3 d = vec3(4.086 ,2.624 ,3.019);

    return a + b*cos(6.28318*(c*t*d));
}

void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy)/ u_resolution.xy;
    vec2 uvo = uv;
    vec3 fincol = vec3(1.0);

    float t = u_time;

    float d = length(uv);
    float x = uv.x;
    float z = t;
    float y = uv.y; 
    fincol.x = sin(x-z)*cos(y-z)+sin(y-z)*cos(z)+sin(z)*cos(x-z);
    fincol.y = pallete(fincol.x*10.).y;
    //fincol.y *= exp(d*u_time);

    //fincol = vec3(log(d+u_time),cos(d),1);

    gl_FragColor = vec4(fincol,1.0);
}