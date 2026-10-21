## Air Temperature Measurement Errors in Naturally Ventilated Radiation Shields

REINA NAKAMURA AND L. MAHRT

*College of Oceanic and Atmospheric Sciences, Oregon State University, Corvallis, Oregon*

(Manuscript received 2 September 2004, in final form 19 January 2005)

## ABSTRACT

Two sources of systematic errors are considered for estimating air temperature. The first source is ambiguity of the definition of the standardized measurement height over vegetated surfaces of varying heights. Without such a standardization, evaluation of the horizontal air temperature gradient is contaminated by the vertical variation of air temperature. This error is generally small in daytime unstable conditions, but increases with increasing stability at night. In an attempt to reduce such error, the use of the zero-plane displacement height for standardizing the measurement height is proposed.

The second source of systematic errors is radiative forcing on the sensor–shield systems. A series of experiments is performed over a grass field to investigate the radiatively induced error in the air temperature estimate by the Onset HOBO Pro thermistor in a naturally ventilated multiplate shield. The magnitude of this error is estimated by comparing air temperature measurements by a platinum resistance temperature detector (RTD) sensor in a mechanically aspirated shield. In contrast to the errors resulting from the first source, the radiatively induced error increases with increasing instability. An empirical model is developed for correcting the radiatively induced temperature error using information on wind speed and net or shortwave radiation. The robustness of the model is examined with independent data.

## 1. Introduction

With advancement in technology, both temperature sensors and dataloggers have become less expensive, less power consuming, portable, robust, and reliable for long-term field deployment. To minimize the influence of shortwave radiation and longwave radiative exchange, a temperature sensor needs to be enclosed in a radiation shield. While an ideal radiation shield would be mechanically aspirated, the cost and power requirements of such systems remain prohibitively high for most long-term network deployments.

A mechanically aspirated radiation shield is often replaced by a naturally ventilated radiation shield in such observational networks. When radiative forcing on the radiation shield is large and the ambient wind is weak, ventilation becomes inadequate to avoid significant radiatively induced air temperature errors (e.g., Tanner et al. 1996; Anderson and Baumgartner 1998; Richardson et al. 1999; Lin et al. 2001b; Erell et al. 2005). These errors need to be assessed for correctly interpreting air temperature data collected in a naturally ventilated shield. For example, if sensor–shield systems within a network of air temperature measurements experience different radiative forcing because of variable cloudiness or exposure differences, the horizontal temperature gradient may be incorrectly estimated because of the spatial variation of errors. In addition, when air temperature measurements are used to evaluate the sensible heat flux from the surface with the bulk transfer method, radiatively induced errors could cause significant errors in the predicted sensible heat flux and even the wrong sign (Anderson and Baumgartner 1998; Arck and Scherer 2001).

The HOBO Pro datalogger (Onset Computer Corporation model H08–031–08) and its external thermistor (Whiteman et al. 2000), which is enclosed in a naturally ventilated multiplate radiation shield, is one of the practical and economical systems for long-term air temperature monitoring. The HOBO logger and thermistor are durable for the outdoor environments, require minimal power, and operate with relatively high accuracy. In this study, the radiatively induced error of air temperature measurements (radiative error, hereafter) by this thermistor in a multiplate shield is investigated

*Corresponding author address:* Reina Nakamura, Department of Meteorological Environment, Forestry and Forest Products Research Institute, 1 Matsunosato, Tsukuba, Ibaraki 305-8687, Japan. E-mail: reina@affrc.go.jp

and a correction formula is constructed. Before examining the radiative error, we first investigate ambiguity of the definition of the standard measurement height over vegetation of varying height as a source of systematic errors on air temperature.

2. Standardizing the height of air temperature measurements

Even with perfect instrumentation, air temperature measurements are often characterized by a certain degree of ambiguity because of the uncertain interpretation of the influence of the upwind heterogeneity of the surface on the temperature measurement and by the uncertain choice of measurement height above vegetated surfaces. We examine the ambiguity of air temperature measurements of the latter kind. A standard measurement height may be defined without ambiguity over flat terrain with bare soil or very short uniform vegetation. However, when the ground surface is covered by nonuniform vegetation, such as grass, shrubs, and trees, the definition of the standard height may become ambiguous. For example, it is not meaningful to compare air temperature at 1 m above the bare ground with a second air temperature at 1 m above the ground surface, but only slightly above the top of the vegetation.

A representative measurement of air temperature is best made in the surface layer above the influence of horizontal variation of mean temperature on the horizontal scale of the roughness elements, that is, above the roughness sublayer (e.g., Kaimal and Finnigan 1994). Within the surface layer, the height dependence of air temperature is governed by turbulent momentum and heat fluxes according to the Monin–Obukhov similarity theory, such that (Brutsaert 1982)

<!-- reconstructed: verify against p.2 ((1) k -> kappa) -->
$$\bar{\theta} = \bar{\theta}_s - \frac{\overline{w'\theta'}}{\alpha_h \kappa u^*} \left[ \ln\left(\frac{z - d_o}{z_{oh}}\right) - \psi_h\left(\frac{z - d_o}{L}\right) \right], \quad (1)$$

where $z$, $\bar{\theta}$, $\bar{\theta}_s$, $\bar{w}'\theta'$, $\alpha_h$, $\kappa$, $u^*$, $d_o$, $z_{oh}$, $\psi_h$, and $L$ are the measurement height above the ground surface, the mean potential air temperature at height $z$, the aerodynamic surface temperature, sensible turbulent heat flux, the ratio of the eddy diffusivity for heat to that for momentum (taken to be unity for this study), the von Kármán constant, the friction velocity, the zero-plane displacement height, the roughness length for sensible heat, a stability function for sensible heat transfer, and the Obukhov length, respectively. The friction velocity is defined as (Stull 1988)

$$u^* = (\overline{u'w'}^2 + \overline{v'w'}^2)^{1/4}, \quad (2)$$

where *uw* and *w* indicate the vertical turbulent momentum flux in the along- and crosswind directions.

The Obukhov length is defined as

<!-- reconstructed: verify against p.2 ((3) mu -> u, overbar on flux) -->
$$L = - \frac{\overline{\theta_v} u^{*3}}{\kappa g \overline{w' \theta_v'}}. \quad (3)$$

We use the $\psi$ stability function in Brutsaert (1982).

We propose the standard measurement height to be a fixed height above the displacement height *do*, not above the ground surface, in order that the relative vertical variations of the mean temperature do not contaminate the estimation of the horizontal variations. The variable height of the sensor above the ground surface is

$$z = Z + d_o, \quad (4)$$

where *Z* is the prescribed fixed height of the sensor above the variable displacement height. The displacement height *do* depends, in part, on the way the drag force is distributed through foliage (Kaimal and Finnigan 1994). The displacement height has been related to the roughness density (Raupach 1994). At the same time, prediction of the displacement height *do*, based only on the canopy architecture, remains uncertain (Monteith and Unsworth 1990). As a rule of thumb, for uniform vegetation, one might use 2/3–3/4 of the vegetation height (Parlange and Brutsaert 1989; Jones 1992), although much smaller values may be more suitable for sparse canopies. In practice, the displacement height *do* must be estimated from profiles and/or eddy correlation measurements (e.g., De Bruin and Moore 1985). However, even with such measurements, there is no general agreement on the precise method for estimating the displacement height. In many studies, neither the profiles nor eddy correlation data are available. The estimated displacement height *do* estimated can be expressed as

$$d_o \text{ estimated} = d_o + d_o \text{ error}, \quad (5)$$

where *do* error denotes the uncertainty in the estimated displacement height, including the failure to account for growing vegetation. The temperature sensor is deployed at

$$z = d_o \text{ estimated } + Z = d_o + Z + d_o \text{ error} \quad (6)$$

Thus, the error in the displacement height *do* error directly translates into deviation of the measured temperature from the required temperature at the standard height *Z* above the true displacement height *do* (Fig. 1).

Using Eq. (1), the error in the estimated air temperature measurement for the standard height *Z* can be written as

$$\begin{aligned} \bar{\theta}(Z + d_{o\text{ estimated}}) - \bar{\theta}(Z + d_o) = \\ - \frac{\overline{w'\theta'}}{\alpha_h \kappa u^*} \left[ \ln \left( \frac{Z + d_{o\text{ error}}}{z_{oh}} \right) - \ln \left( \frac{Z}{z_{oh}} \right) \right. \\ \left. - \psi_h \left( \frac{Z + d_{o\text{ error}}}{L} \right) + \psi_h \left( \frac{Z}{L} \right) \right]. \end{aligned} \quad (7)$$

To illustrate the influence of an inappropriately estimated zero-plane displacement height on the measured air temperature, a heuristic exercise is performed with sonic anemometer data from the Flux Over Snow Surface II (FLOSS II; Mahrt and Vickers 2005). We analyze eddy correlation data collected at 2 m above the ground surface where the average height of the sparse brush is $h_{\text{avg}} = 0.3$ m, although the actual height of the brush varies between 0.2 and 0.6 m. The data were collected at 20 Hz at 2 m above the ground surface ($z = 2$ m). Turbulent heat and momentum fluxes are computed with an averaging window of 150 s. The flux data are averaged over 1 h to reduce random flux sampling errors. No data are analyzed for the transition periods (0700–1000, 1500–1800 LST) to avoid the influence of nonstationarity. The thermal roughness length ($z_{oh}$) is

set equal to the momentum roughness length ($z_{om} = 0.039$ m), where the latter is determined in near-neutral conditions. As with most datasets, we cannot confidently estimate the displacement height, but can only show sensitivity of the measured air temperature at $Z + d_o$, to the estimated displacement height $d_o$ estimated. As an instructive example, we consider $d_o = 1/2 h_{\text{avg}} = 0.15$ m as a plausible displacement height for a sensitivity calculation.

The air temperature error for a measurement height of $Z = 1.85 \text{ m}$ ($Z + d_o = z = 2 \text{ m}$) is simulated with Eq (7) for a range of errors in the estimated displacement height (Fig. 2). For this sensitivity exercise, the maximum positive value of the estimated displacement height is $2/3$ of the maximum vegetation height of $h_{\max} = 0.6 \text{ m}$. This range of the estimated displacement heights changes the temperature measurement as much as $0.2^\circ\text{C}$ in stable conditions, but is much less for unstable conditions. This temperature error can, for example, lead to large errors in the horizontal advection computed over small distances (Ha and Mahrt 2003) or in the surface sensible heat flux computed with the bulk transfer method. The air temperature measurement error

FIG. 1. Illustration of an unstable vertical temperature profile in the atmospheric surface layer. Estimated displacement height $d_o$ estimated is shown as $d_o + d_o$ error; $\theta$ indicates potential temperature: $\theta_s$ indicates the aerodynamic surface temperature.


ror can become even larger if the plausible range of the displacement height estimate increases because of an increase in the range of vegetation height. Because the vertical gradients increase toward the "surface," the problem of the incorrectly estimated displacement height becomes more serious for measurements closer to the surface.

The air temperature errors resulting from the height uncertainty limit the advantage of expensive aspirated sensor–shield systems. Thus, an accurate estimate of the displacement height for a vegetated surface is important, which suggests a need for an improved methodology to estimate the displacement height, particularly over nonuniform vegetation.

## 3. Instrumentation and data

The details of instrumentation used in our field experiments are summarized in Table 1. The HOBO Pro datalogger (model H08–031–08) is a two-channel logger, equipped with two thermistors—an internal thermistor and an external thermistor connected by the logger unit with a 1.7-m cable. The manufacturer’s specification states that the HOBO logger with a replaceable small lithium battery is able to operate continuously for up to 3 yr unless operated at very low temperatures. In this study, we use only the external thermistor (the HOBO thermistor hereafter). Our indoor experiments determined the time constant of the HOBO thermistor in still air to be 180 s, between that reported by the manufacturer’s specification (270 s) and that by Whiteman et al. 2000 (112 s). With a mechanical aspiration of 3–7 m s<sup>-1</sup>, however, the time constant of the HOBO thermistor improves to approximately 26 s. The present study investigates radiative errors in the mean air temperature over 30-min periods estimated by the HOBO thermistor, operating in a high-resolution mode in an outdoor field situation. The thermistor is enclosed in the naturally ventilated multiplate shield manufactured by Davis Instruments (model 7714). This multiplate shield is also known as the solar radiation shield RS1 of Onset Computer Corporation (Fig. 3). A sampling interval of 300 s is selected for the HOBO thermistor, which allows the logger to collect data for 3–4 months.

Data were collected above a flat grassland (latitude: 44°38N, longitude: 123°12W) in the spring and summer of 2002 and in the summer of 2003. As basic

Fig. 2. Simulated bin-averaged error in estimated temperature for $z = Z + d_o + d_o^{\text{error}}$ due to nonzero $d_o^{\text{error}}$ as a function of stability for various errors in the displacement height; $Z$ is set to 1.85 m. The bin width in $(z - d_o)/L$ is 0.25. The vertical bars indicate the standard error within each bin. The true displacement height $d_o$ is 0.15 m in this exercise. Solid line: $d_o^{\text{error}} = -0.15$ m ($d_o + d_o^{\text{error}} = 0$ m), dashed line: $d_o^{\text{error}} = 0.05$ m ($d_o + d_o^{\text{error}} = 2/3h_{\text{avg}} = 0.2$ m), dashed-dotted line: $d_o^{\text{error}} = 0.2$ m ($d_o + d_o^{\text{error}} = 2/3h_{\text{max}} = 0.45$ m).

TABLE 1. Summary of the instrumentation.

| Sensors | Manufacturer and model | Manufacturer's specification |
|---|---|---|
| Thermistor and logger | Onset, 08-03-08 | Thermistor dimension: 5 mm (diameter), 30 mm (height); time constant: 270 s; accuracy: $\pm 0.2^\circ$ C; logger time drift $\pm 100$ s per week at 20°C |
| Plantinum RTD | RM Young, 43347 | Dimension: 3.2 mm (diameter), 57 mm (height); time constant: 42 s; aspiration accuracy: $\pm 0.1^\circ$ C |
| Aspirated radiation shield | RM Young, 43408 | Airflow rate 3-7 m s <sup>-1</sup> , depending on sensor size; radiation error: $<0.2^\circ$ C at 1100 W m <sup>-2</sup> |
| 2D sonic anemometer | Vaisala, WS425 | Resolution: 0.1 m s <sup>-1</sup> ; accuracy: $\pm 0.135$ m s <sup>-1</sup> |
| Net radiometer | Kipp and Zonen, CNR1 | Response time: 18 s; spectral response: 305-2800 nm (pyranometer), 5000-50 000 nm (pyrgeometer); pyranometer error: $<25$ W m <sup>-2</sup> |
| Silicon pyranometers | Licor, Li-200S | Response time: 10 $\mu$ s; spectral response: 400-1100 nm; error in natural daylight: $\pm 3\%$ |
| Infrared transducers | Apogee, URTS-P5 | Response time: $<1$ s; accuracy: $\pm 0.2^\circ$ C |
| Type-E thermocouple | Campbell, FW3 | 0.076 mm; response time: a few ms |


datasets (datasets A and B), air temperature was measured by 1) a HOBO thermistor in the Davis multiplate shield and 2) a platinum resistance temperature detector (RTD) sensor in a mechanically aspirated shield (RM Young model 43408), with both at 1 m above the ground surface. The horizontal separation distance between the two sensors was approximately 1.5 m. In addition, wind speed, wind direction, and upward and downward components of shortwave and longwave radiation were measured. Table 2 summarizes these data and other datasets acquired during the field experiment, which are analyzed in later sections.

All the data except for the HOBO thermistor mea-

surements, were logged at 0.5 Hz by a Campbell Scientific CR23X datalogger in 2002 and CR5000 datalogger in 2003. All the temperature sensors were thoroughly intercompared at 0°C in an ice bath and at room temperature. Small offsets of individual sensors of less than a tenth of a degree Celsius are corrected for all the analyses below.

## 4. Sources of radiative errors

## *a. General considerations*

The energy balance on a temperature sensor consists of shortwave radiative forcing, longwave radiative exchange, and sensible heat transfer between the sensor and the surrounding air. The radiative error can be often reduced by decreasing the sensor size (Campbell 1969). However, the need for durability and economy in long-term field experiments generally requires the use of a larger sensor.

To minimize the influence of shortwave radiation and longwave radiative exchange with the surroundings, such as clear sky and ground surface, the sensor is deployed within a radiation shield. An ideal naturally ventilated shield should prevent shortwave radiation from penetrating into the interior. The ray-tracing study of Richardson et al. (1999) showed that shortwave radiation entering a multiplate shield is mostly absorbed by the shield or sensor rather than exiting the sensor–shield system, thus, contributing to the radiative error.

Deviation of the shield temperature from the air temperature can also become a source of radiative error in that it modifies the air temperature inside the shield by sensible heat transfer from the plates and modifies the sensor temperature by longwave radiative transfer. The

FIG. 3. Cross section of Davis Instruments multiplate shield model 7714 (Onset Computer Radiation Shield RS1). Dimension of the shield is 213 mm (length) 188 mm (depth) 152 mm (height). Individual plates are 3 mm thick. All of the plates are separated by 15 mm, except for the top two, which are separated by 20 mm. The vertical overlap between a plate and the one underneath is 4 mm.

TABLE 2. Summary of data collection. Height is above the ground surface unless otherwise noted. Here MS and MAS stand for multiplate shield and mechanically aspirated shield, respectively.

| Dataset ID | Dates | Data type | Height (m)/position | |
|---|---|---|---|---|
| A | 14 Mar–30 Aug 2002 | Air temperature | HOBO thermistor in MS | |
| | | | RTD in MAS | |
| | | Wind speed/direction | 1.5 | |
| | | Four-component radiation | | |
| | | Same as dataset A | | |
| B | 15 Jul–30 Aug 2003 | Downward shortwave | Grass | 0.025 from MS inner |
| C | 30 Jul 2003 | irradiance in MS | Black tarp | bottom |
| | 1 Sep 2003 | | White tarp | |
| | 1 Sep 2003 | | | |
| | 13 Aug 2003 | Upward shortwave | Grass | 0.035 from MS inner |
| | 2 Sep 2003 | irradiance in MS | Black tarp | bottom |
| | 2 Sep 2003 | | White tarp | |
| D | 15 Jul–30 Aug 2003 | MS surface temperature | Infrared transducers | MS outer top and bottom |
| | | | Thermocouple | MS outer top |


shield temperature can be maintained closer to the air temperature by choosing appropriate material and coating for the shield (Fuchs and Tanner 1965).

The sources of radiative error for the shield–sensor system are counteracted by increasing the degree of coupling of the air inside the shield to the ambient air. Unfortunately, increasing coupling requires a wider separation distance between the shield plates and, therefore, more direct shortwave radiation into the shield interior and possibly more longwave radiative exchange between the sensor and objects outside the shield.

*b. Imperfect shielding of shortwave radiation*

The degree of shortwave radiation reaching inside a radiation shield may be represented as the mean shortwave radiation ratio *S*\* (%), based on Hubbard et al. (2001), defined as

$$\overline{S^*} = 0.5(S^* \downarrow + S^* \uparrow), \quad (8)$$

where $S^* \downarrow$ and $S^* \uparrow$ are downward and upward shortwave radiation ratios (%), respectively, defined as

$$S^* \downarrow = \frac{\text{Downward shortwave irradiance inside shield}}{\text{Downward global shortwave irradiance outside shield}} \times 100, \quad (9)$$

and

$$S^* \uparrow = \frac{\text{Upward shortwave irradiance inside shield}}{\text{Downward global shortwave irradiance outside shield}} \times 100. \quad (10)$$

To estimate the downward and upward shortwave irradiance inside the Davis multiplate shield during the daytime, a pair of Licor Li-200S pyranometers were deployed inside the multiplate shields (dataset C). Because the vertical dimension of the space inside the shield is only 7.0 cm in height, only one pyranometer (2.5-cm height) is deployed within a shield at a time. Thus, downward and upward shortwave radiation within a particular shield was measured on separate days. Downward (upward) shortwave radiation measurements were made by an upward (downward)-facing pyranometer situated at a 2.5-cm (3.5 cm) height above the next lowest plate. It was technically difficult to install a pyranometer at other heights without significantly blocking the path of the shortwave radiation. However, these measurement heights of the pyranometers fall in the height range over which the HOBO thermistor inside a shield typically extends (2.5–6 cm above the next lowest plate). The spectral distribution of shortwave radiation inside the multiplate shield dif-


fers from that under direct shortwave radiation. The effect of altered spectral distribution is taken into account for the pyranometer data by adopting the calibration formula determined by Hubbard et al. (2001).

To investigate the influence of shortwave radiation reflected from the ground surface, pyranometers enclosed in the multiplate shields were deployed over three surface types: the original grass, a black surface, and a white surface. The black and white surfaces were created by a single black plastic sheet (0.08 mm thick) and by eight layers of transparent sheets (each 0.025 mm think), respectively. The size of both sheets was 6 m 6 m. The multiplate shields were deployed in the center at 1 m above the ground surface. The individual plates of the present multiplate shield are rectangular (0.188 m 0.213 m), so that the area-based equivalent square would be exactly 0.20 m on a side. Such a plate located 1 m above the ground receives 92% of the entire radiation from the ground surface of 6 m 6 m if the surface is assumed to be a diffuse surface (Howell 1982). A diffuse surface is defined as a surface that emits and/or reflects equal radiation intensity in all directions. The measured albedos of the black, grass, and white surfaces are 0.08, 0.23, and 0.56, respectively.

Figure 4a illustrates $\overline{S^*}$ over the grass, black, and white surfaces. The $\overline{S^*}$ values are computed from $S^*\downarrow$ and $S^*\uparrow$ measured on two different cloudless days. Both ratios $S^*\downarrow$ and $S^*\uparrow$ reach maximum values at large solar zenith angles, although the absolute magnitude of the shortwave radiation that is detected inside the shield at such zenith angles is at a minimum. Richardson et al. (1999) reported a similar finding in a numerical ray-tracing study within a Gill multiplate shield (Gill

FIG. 4. (a) Mean shortwave radiation ratio $\overline{S}^*(\%)$, and (b) difference between the downward shortwave radiation ratio and the upward shortwave radiation ratio $\overline{S}^* \downarrow - \overline{S}^* \uparrow$ (%) for grass-covered (o), black ($\Delta$), and white ($\nabla$) surfaces. Negative (positive) sign in the solar zenith angle indicates before (after) solar noon.

1979). Shortwave radiation reaching inside the shield is positively correlated with surface albedo (Fig. 4a). The midday value of *S*\* becomes 1.4%, 2.3%, and 3.1% for black, grass, and white surfaces, respectively. Over the white surface *S*\* is typically twice as large as that over the black surface except for its high solar zenith angle. This result implies that a significant portion of shortwave radiation reaching inside the shield originates from shortwave radiation reflected from the ground surface. The radiative error resulting from the heating of the sensor by its absorption of shortwave radiation inside the present multiplate shield likely increases with increasing albedo.

The difference between $S^*\downarrow$ and $S^*\uparrow$ is generally small, except when the solar zenith angle exceeds about $70^\circ$ (Fig. 4b). This result may indicate that a large portion of shortwave radiation detected inside the shield during midday may be diffuse rather than direct. Richardson et al. (1999) argues that shortwave radiation that is reflected from an imperfectly smooth shield plate surfaces yields diffuse radiation. A part of the difference between the observed $S^*\downarrow$ and $S^*\uparrow$ may also be attributed to the exact position of the pyranometer with respect to the shield structure (Hubbard et al. 2001).

## *c. Shield surface warming/cooling*

A shielded thermistor exchanges longwave radiative energy with the inner surface of the shield. However, we were able to measure only the temperature of the outer surface of the Davis multiplate shield with existing instrumentation. We assume that the conductivity of the shield material is sufficiently high so that changes of the inner and outer surface temperatures of a given plate are highly correlated. An infrared transducer (Apogee IRTS-P5) is deployed directly above and underneath a multiplate shield. In addition, a type-E thermocouple is fixed to the top plate of another multiplate shield that is located 0.7 m away from the first shield (dataset D). For the true air temperature estimate, air temperature data from the aspirated RTD sensor of dataset B are employed.

The shield-top temperature measured by the thermocouple and that measured by the IR transducer agree at night within a few tenths of a degree Celsius (Fig. 5). However, the thermocouple measurements become significantly larger than the IR transducer measurements during daytime. This difference may be explained by the combination of a self-shadowing effect of the IR transducer at low solar zenith angle and shortwave heating of the thermocouple wires. The actual shieldtop daytime temperature is tentatively considered to be somewhere between these two estimates.

Because the outer surface of the shield is directly exposed to external radiation, the thermistor inside the multiplate shield is expected to be much less influenced by external radiation than the outer surface. Therefore, the radiatively induced temperature excess or deficiency of the outer shield is expected to be substantially larger than the radiatively induced thermistor error, as verified in the next section.

5. Correction of radiatively induced temperature errors

The radiative error resulting from radiative heating or cooling of the sensor is reduced by airflow past the

FIG. 5. Bin-averaged deviation of the shield surface temperature from air temperature as a function of net radiation above the grass surface. The shield-top temperature was simultaneously monitored by a thermocouple (gray) and an infrared transducer (black). Vertical bars indicate standard errors within bins.


force surface, which enhances sensible heat transfer between the sensor and surrounding air (section 4a). Rigorous correction of radiative errors may require radiation and airflow measurements inside the shield which are not necessarily linearly correlated with those outside the shield. Richardson et al. (1999) simulated flow in and around the Gill multiplate shield and found that the flow efficiency, the fraction of the ambient wind speed that is detected inside, decreases with decreasing ambient wind speed, especially for ambient wind speeds less than $1\text{ m s}^{-1}$. To the contrary, the flow efficiency increased slightly when the ambient wind speed is reduced down to $0.5\text{ m s}^{-1}$ in laboratory and field studies with the Maximum–Minimum Temperature System (MMTS) multiplate radiation shield (Lin et al. 2001a). The behavior of the flow efficiency as a function of the ambient wind speed appears to be quite complex, and depends on the exact design of the multiplate shield and even on the characteristic of the flow, such as steadiness and turbulent intensity (Lin et al. 2001a). In practice, simpler procedures are desirable for routinely correcting the radiative error without explicitly assessing the flow efficiency. We attempt to pragmatically correct for the radiative error using only information on wind speed and shortwave or net radiation measurements made outside the shield.

The radiative error is often modeled in terms of low Reynolds turbulent heat transfer between the sensor or the shield surface and the ambient atmospheric air (e.g., Tanner 1979; Anderson and Baumgartner 1998; Erell et al. 2005). Unlike in laboratory settings, the turbulence that is responsible for the heat transfer between an obstacle and the atmosphere is normally strongly influenced by ambient high Reynolds atmospheric turbulence, in addition to turbulence induced by the obstacle, which may not be low Reynolds turbulence as has previously been assumed. Atmospheric eddies that are larger than the length scale of the obstacle act like a time-dependent mean wind imposed on the obstacle and its energy exchange with the atmosphere. Such eddies trigger transient internal boundary layers at the surface of the obstacle. The depth of the obstacle internal boundary layer is inversely related to the wind speed (Incropera and De Witt 1990). Atmospheric eddies of the same size as the obstacle may distort or disrupt the obstacle internal boundary layer. Atmospheric eddies that are small compared to the obstacle have a dissipative influence on the turbulent eddies that are generated by the obstacle. Therefore, heat transfer between a sensor or shield and the atmosphere in fully developed turbulence cannot be exclusively related to the Reynolds number or molecular properties of the airflow, as attempted in the past literature. However,


heat transfer between the sensor surface and air within a multiplate shield may be governed by low Reynolds turbulence. The low Reynolds turbulence is generated not only by the sensor itself, but also by individual plates and plate spacers. Thus, characteristic length scales of these objects influence the heat transfer between the sensor surface and air inside the shield. We do not attempt to model these complex processes, but rather construct a simpler and more empirical approach.

## *a. HOBO radiative error*

We assume that the radiative error for the RTD sensor in the mechanically aspirated shield is small compared to that for the HOBO thermistor. The difference between the HOBO and the mechanically aspirated RTD temperature measurements is considered to be the HOBO radiative error, which will be related to the ambient radiation and wind speed (dataset A). An averaging interval of 30 min is selected for this study. The manufacturer's specification states that the shortwave radiation measurements by the CNR1 net radiometer (Table 1) are unreliable when the solar zenith angle is greater than $80^\circ$. Therefore, such data are discarded. We use scalar- rather than vector-averaged wind speeds over 30 min because the magnitude of the instantaneous wind speed, regardless of the wind direction, ventilates the sensor-shield system.

During the daytime, the HOBO radiative error becomes systematically positive with shortwave radiation (Fig. 6). At night, when the net radiation is negative,

FIG. 6. The original (gray circle) and bin-averaged values (black circle) of the HOBO radiative errors for all the data. The error bars indicate the standard errors. The bin width is $20 \text{ W m}^{-2}$ except all the HOBO radiative errors in shortwave radiation of $0 \text{ W m}^{-2}$ (nighttime) are averaged together.

the HOBO radiative error generally becomes weakly negative. Thus, we attempt to correct the radiative errors separately for the daytime and nighttime periods. The radiative error is larger during the daytime, with an average value of 0.39°C; the radiative error becomes larger than 0.5° and 1.0°C for 22.9% and 2.6% of the daytime periods, respectively. The mean nocturnal radiative error is only -0.002°C, but the error increases systematically with increasing radiative forcing (Fig. 7, section 5b). The radiative error becomes larger than -0.5°C for only 4.6% of the nocturnal periods.

## *b. Similarity regression model*

We propose expressing the radiative error in terms of the ratio of the radiative forcing to the natural ventilation represented by the nondimensional number,

$$X = \frac{\text{Rad}}{\rho C_p T_{\text{HB}} U}, \quad (11)$$

where Rad ($\text{W m}^{-2}$) indicates shortwave radiation and net radiation for the daytime and nocturnal periods, respectively; $U$ is the wind speed ($\text{m s}^{-1}$); $\rho$ is the density of air, taken to be $1.2 \text{ kg m}^{-3}$; and $C_p$ is the specific heat capacity of air at constant pressure, taken as $1004 \text{ J K}^{-1} \text{ kg}^{-1}$. The HOBO air temperature measurement, denoted by $T_{\text{HB}}$, is expressed in kelvins. The relationship between the radiative error RE and nondimensional radiative forcing $X$ is expressed as a polynomial function,

$$\text{RE} = C_0 + C_1 X + C_2 X^2 \cdots, \quad (12)$$

where $C_0$, $C_1$, and $C_2$ are empirical coefficients that presumably depend on characteristics of the sensor-shield system and those environmental flow characteristics that are not included in $X$.

The radiative error correction is most needed when the wind is weak and radiative forcing is strong (section 4b), that is, when $X$ is large (Fig. 7). However, such conditions occurred less frequently than conditions with significant wind or cloudiness, corresponding to smaller radiative errors. Therefore, to retain an appreciable influence of cases with large $X$ in the determination of the coefficients of the model in Eq. (12), the original 30-min data of the HOBO error are averaged for intervals or bins of the nondimensional radiative forcing $X$. The width of the bins is set to $1.25 \times 10^{-4}$ and $2.5 \times 10^{-5}$ for daytime and nighttime periods, respectively. These bin widths yield approximately 20 bins. We require at least five data points within a bin for the averaging procedure. The result of the analysis below is insensitive to the exact width of the bin. Equation (12) is regressed on the bin-averaged data.

The $R$ -squared value, that is, the fraction of variance explained by a model, always improves by adding more terms. Therefore, the statistical significance of the $R$ -squared value is examined with the analysis of variance after each higher-order term is added to the model (e.g., Chelton 1983). The hypothesis that an additional term did not improve the true regression model is tested with the $F$ test at the 95% confidence level by assuming that the individual bin-averaged data are statistically independent. The results indicate that adding higher-order terms beyond the first-order term does

Fig. 7. HOBO radiative error as a function of nondimensional radiation forcing $X$. For display, the radiation forcing in the horizontal axes has been multiplied by $10^3$ and $10^4$ for day and night, respectively. SW and Rnet stand for shortwave and net radiation, respectively. Lines indicate regression lines based on the coefficients in Table 3.


not improve the regression model with statistical significance. The *R*-squared value of the determined model is 0.98 and 0.94 for the daytime and nighttime, respectively. These values are much higher than the 95% critical values for the *R*-squared value of the model under the null hypothesis—0.21 for the daytime and 0.19 for the nighttime.

The procedure adopted for determining the coefficients maximizes the $R$ -squared value over the entire range of the radiative forcing $X$ in terms of a linear fit. For both daytime and nighttime, the coefficients that are determined from this procedure (Table 3) yield a nonzero constant as the radiative forcing $X$ vanishes. The nonzero correction at $X = 0$ is, therefore, an artifact of the statistical fit. For nighttime, the nonzero constant is a few hundredths of a degree, which is sufficiently close to zero so that we apply the determined coefficients for correcting the HOBO air temperature measurements for the entire range of nighttime $X$. For daytime, Fig. 7 indicates that the fit suddenly breaks down for very small values of $X$ less than $1.0 \times 10^{-4}$, and we suggest that the small corrections for $X$ less than $1.0 \times 10^{-4}$ be neglected. The percentage of the neglected data corresponds to 3.1% of all the daytime data.

The regression model with the estimated coefficients is used to correct the original HOBO air temperature measurements. The radiative error is substantially reduced after the correction, especially in weak wind and sunny conditions (Fig. 8). The correction reduces the mean and the root-mean-square errors in both periods, particularly in the daytime when the errors are larger (Table 4). For nocturnal periods, the model does not lead to significant improvement for the dataset as a whole. This is because the nocturnal HOBO errors are dominated by $X > -3 \times 10^{-4}$, where the errors are random with a near-zero mean (Fig. 7).

The present model does not include all of the physical processes affecting the radiative error, which partly accounts for the remaining error. For example, for a given ambient wind speed, the dependence of the flow rate in the shield on characteristics of the ambient wind (e.g., airflow steadiness and turbulence intensity) is not included in the model. As an additional example, change in the cloud cover within the averaging time is not considered. Finally, the aspirated RTD sensor may also be subject to nonnegligible errors.

## *c. Robustness of model*

The robustness of the error-correction model and coefficients that are determined with dataset A are now tested with dataset B collected at the same site, but in the summer of 2003 (Table 2). The radiative errors are effectively reduced for dataset B, indicated by the reduced mean and root-mean-square errors (Table 5). In spite of the fact that the coefficients are calibrated using the 2002 data, the correction model is effective for 2003 data. Because the intensity of shortwave forcing is influenced by the ground surface albedo (section 4b), the coefficients that are determined in this study may not be optimum for surface types other than grass.

## 6. Summary

We propose that measurements of air temperature be made at a standard measurement height above the zero-plane displacement height. This standardization is necessary for eliminating the ambiguity of definitions of sensor-deployment heights, particularly above vegetation of varying height. Otherwise, the estimation of the horizontal variations of air temperature is contaminated with the relative vertical variations of the mean temperature. In addition, the sensible heat flux estimates with the bulk transfer method are subject to errors. The air temperature measurement error resulting from incorrectly estimated displacement heights is small in daytime unstable conditions, but increases with increasing stability at night. The error resulting from incorrectly estimated displacement heights limits the advantage of expensive aspirated sensor–shield systems. An improved methodology to estimate the displacement height is required, particularly over nonuniform vegetation.

Within observational networks of air temperature, temperature sensors are often deployed in naturally ventilated shields instead of mechanically aspirated radiation shields because of economical considerations and the unavailability of power. This study evaluates the radiative error of air temperature measurements by the HOBO thermistor in the Davis Instruments multiplate radiation shield, also known as the Onset Computer radiation shield. This sensor–shield system is one of the practical and economical naturally ventilated sensor–shield systems.

Our measurements indicate that shortwave radiation reaching inside the multiplate shield increases with increasing albedo of the surface. A significant portion of

TABLE 3. Summary of determined coefficients for the similarity regression model for daytime and nighttime periods.

| | Relevant radiation data | C 0 | C 1 |
|---|---|---|---|
| Day | Shortwave | 0.13 | 373.40 |
| Night | Net | 0.047 | 355.84 |

FIG. 8. Bin-averaged HOBO radiative errors for 30-min mean air temperature as a function of (a) wind speed, (b) shortwave or net radiation, and (c) nondimensional radiative forcing *X* [Eq. (11)] for (left) daytime and (right) nighttime. For display, the radiation forcing in the horizontal axes has been multiplied by 103 and 104 for day and night, respectively. Gray and black HOBO errors indicate those before and after corrections [Eq. (12)], respectively. The vertical bars indicate the standard error within each bin.


shortwave radiation inside the shield originates from shortwave radiation reflected from the ground surface. Thus, radiatively induced temperature errors probably increase with increasing surface albedo. The magnitude of the deviation of the shield surface temperature from the air temperature usually becomes larger during the daytime with shortwave forcing than during the nighttime. With this effect, and shortwave radiation reaching inside the shield during the daytime, the radiative error of the air temperature measurement by the sensor– shield system becomes more significant during the daytime than during the nighttime. This diurnal trend is the opposite to that of the error resulting from inadequately evaluated zero-plane displacement heights. The daytime radiative error becomes large, especially in conditions of weak wind and significant shortwave radiation. The radiative error decreases rapidly with increasing wind speed, which ventilates the sensor– shield system.

An empirical correction is proposed based on a nondimensional number that is proportional to the daytime shortwave or nocturnal net radiation and is inversely proportional to the wind speed, both of which are measured outside of the multiplate shield. Application of the model substantially reduces both the mean and root-mean-square of the radiative errors of the sensor– shield system, particularly for daytime unstable conditions. Radiative errors for the nighttime stable conditions are much smaller than those for daytime and are likely smaller than the errors resulting from height selection over variable vegetation. The robustness of the radiative error-correction model is confirmed from independent data.

*Acknowledgments.* The authors wish to thank John Wong for his assistance with the field experiment, and Scott Richardson and two anonymous reviewers for their helpful comments on the original manuscript. The authors are grateful to Michael Unsworth for both his assistance in the field and comments on the manuscript. The authors also wish to acknowledge Daryl Ehrensing of the Hyslop Experimental Station for allowing us to conduct field observations in multiple seasons. This work is supported by the NASA Headquarters under the Earth System Science Fellowship, NASA Terrestrial and Ecology Program Grant NAGS5-11231 and Grant ATM-0107617 from the Physical Meteorology Program of the National Science Foundation.

## REFERENCES

Anderson, S. P., and M. F. Baumgartner, 1998: Radiative heating errors in naturally ventilated air temperature measurements made from buoys. *J. Atmos. Oceanic Technol.,* **15,** 157–173. Arck, M., and D. Scherer, 2001: A physically based method for correcting temperature data measured by naturally ventilated sensors over snow. *J. Glaciol.,* **47,** 665–670. Brutsaert, W., 1982: *Evaporation into the Atmosphere.* Kluwer Academic, 299 pp. Campbell, G. C., 1969: Measurement of air temperature fluctuations with thermocouples. Atmospheric Sciences Laboratory, White Sands Missile Range, ECOM-5273, 10 pp. Chelton, D. B., 1983: Effects of sampling errors in statistical estimation. *Deep-Sea Res.,* **30,** 1083–1103. De Bruin, H. A. R., and C. J. Moore, 1985: Zero-plane displacement and roughness length for tall vegetation, derived from a simple mass conservation hypothesis. *Bound.-Layer Meteor.,* **31,** 39–49. Erell, E., V. Leal, and E. Maldonado, 2005: Measurement of air temperature in the presence of a large radiant flux: An assessment of passively ventilated thermometer screens. *Bound.-Layer Meteor.,* **114,** 205–231. Fuchs, M., and C. B. Tanner, 1965: Radiation shields for air temperature thermometers. *J. Appl. Meteor.,* **4,** 544–547. Gill, G. C., 1979: Development of a small rugged radiation shield for air temperature measurements on drifting buoys. National Data Buoy Center, NOAA Rep. Contract 01-7-038- 827, 23 pp. Ha, K.-J., and L. Mahrt, 2003: Radiative and turbulent fluxes in the nocturnal boundary layer. *Tellus,* **55A,** 317–327. Howell, J. R., 1982: *A Catalog of Radiation Configuration Factors.* McGraw-Hill, 243 pp. Hubbard, K. G., X. Lin, and E. A. Walter-Shea, 2001: The effectiveness of the ASOS, MMTS, Gill and CRS air temperature radiation shields. *J. Atmos. Oceanic Technol.,* **18,** 851–864. Incropera, F. P., and D. P. De Witt, 1990: *Fundamentals of Heat and Mass Transfer.* 3d ed. John Wiley & Sons, 919 pp. Jones, H. G., 1992: *Plants and Microclimate.* 2d ed. Cambridge University Press, 299 pp. Kaimal, J. C., and J. J. Finnigan, 1994: *Atmospheric Boundary Layer Flows.* Oxford University Press, 289 pp. Lin, X., K. G. Hubbard, and G. E. Meyer, 2001a: Airflow characteristics of commonly used temperature radiation shields. *J. Atmos. Oceanic Technol.,* **18,** 329–339.

TABLE 4. Statistics of the HOBO errors before and after correction for the radiative error with Eq. (12) for 2002.

| Day | Original | Mean (°C) 0.39 | Root-mean-square error (°C) 0.39 |
|---|---|---|---|
| | Corrected | 0.008 | 0.11 |
| Night | Original |  | |
| | | 0.002 | 0.054 |
| | Corrected | 0.0006 | 0.047 |

TABLE 5. Statistics of the HOBO error before and after correction for the radiative error with Eq. (12) for summer 2003.

| | Root-mean-square | | |
|---|---|---|---|
| | Mean (°C) | | |
| Day | Original | 0.29 | 0.29 |
| | Corrected | −0.08 | 0.13 |
| Night | Original | −0.03 | 0.05 |
| | Corrected | −0.02 | 0.04 |

——, ——, and E. A. Walter-Shea, 2001b: Radiation loading model for evaluating air temperature errors with a nonaspirated radiation shield. *Trans. ASAE,* **44,** 1229–1306. Mahrt, L., and D. Vickers, 2005: Moisture flux over snow with and without protruding vegetation. *Quart. J. Roy. Meteor. Soc.,* **131,** 1251–1270. Monteith, J. L., and M. H. Unsworth, 1990: *Principles of Environmental Physics.* 2d ed. Edward Arnold, 291 pp. Parlange, M. B., and W. Brutsaert, 1989: Regional roughness of the Landes Forest and surface and shear stress under neutral conditions. *Bound.-Layer Meteor.,* **48,** 69–80. Raupach, M. R., 1994: Simplified expressions for vegetation roughness length and zero-plane displacement as functions of canopy height and area index. *Bound.-Layer Meteor.,* **71,** 211–216. Richardson, S. J., F. V. Brock, S. R. Semmer, and C. Jirak, 1999: Minimizing errors associated with multiplate radiation shields. *J. Atmos. Oceanic Technol.,* **16,** 1862–1872. Stull, R. B., 1988: *An Introduction to Boundary Layer Meteorology.* Kluwer Academic, 666 pp. Tanner, B. D., E. Swiatek, and C. Maughan, 1996: Field comparisons of naturally ventilated and aspirated radiation shields for weather station air temperature measurements. Preprints, *22d Conf. on Agricultural and Forest Meteorology,* Atlanta, GA, Amer. Meteor. Soc., 227–230. Tanner, C. B., 1979: Temperature: Critique I. *Controlled Environment Guidelines for Plant Research.,* T. W. Tibbitts and T. T. Kozlowski, Eds., Academic Press, 117–130. Whiteman, C. D., J. M. Hubbe, and W. J. Shaw, 2000: Evaluation of an inexpensive temperature data logger for meteorological applications. *J. Atmos. Oceanic Technol.,* **17,** 77–81.