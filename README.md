# flask-server-demo
server which can handle multiple operations without changing master server. user needs to add only single script in scripts folder based on project requirement.

Example:
post api: http://192.168.1.4:4000/exercise

user will pass api along with script name.
Request:
{
        "scriptName": "excersice1",
        "url": "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly"
    }

Application will read data using api, convert it into pandas dataframe, and in response, html of requested dataframe will be given.

Response:
{
    "data": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>TIME_PERIOD</th>\n      <th>OBS_VALUE</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1999-01</td>\n      <td>0.702913</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1999-02</td>\n      <td>0.688505</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1999-03</td>\n      <td>0.671270</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1999-04</td>\n      <td>0.665018</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1999-05</td>\n      <td>0.658252</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1999-06</td>\n      <td>0.650255</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>1999-07</td>\n      <td>0.657791</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>1999-08</td>\n      <td>0.660136</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>1999-09</td>\n      <td>0.646832</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>1999-10</td>\n      <td>0.645871</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>1999-11</td>\n      <td>0.637018</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>1999-12</td>\n      <td>0.626509</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>2000-01</td>\n      <td>0.618338</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>2000-02</td>\n      <td>0.614657</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>2000-03</td>\n      <td>0.610626</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>2000-04</td>\n      <td>0.598017</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>2000-05</td>\n      <td>0.601509</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>2000-06</td>\n      <td>0.629268</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>2000-07</td>\n      <td>0.623043</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>2000-08</td>\n      <td>0.607096</td>\n    </tr>\n    <tr>\n      <th>20</th>\n      <td>2000-09</td>\n      <td>0.607729</td>\n    </tr>\n    <tr>\n      <th>21</th>\n      <td>2000-10</td>\n      <td>0.589327</td>\n    </tr>\n    <tr>\n      <th>22</th>\n      <td>2000-11</td>\n      <td>0.600386</td>\n    </tr>\n    <tr>\n      <th>23</th>\n      <td>2000-12</td>\n      <td>0.613421</td>\n    </tr>\n    <tr>\n      <th>24</th>\n      <td>2001-01</td>\n      <td>0.634800</td>\n    </tr>\n    <tr>\n      <th>25</th>\n      <td>2001-02</td>\n      <td>0.633995</td>\n    </tr>\n    <tr>\n      <th>26</th>\n      <td>2001-03</td>\n      <td>0.629145</td>\n    </tr>\n    <tr>\n      <th>27</th>\n      <td>2001-04</td>\n      <td>0.621684</td>\n    </tr>\n    <tr>\n      <th>28</th>\n      <td>2001-05</td>\n      <td>0.613282</td>\n    </tr>\n    <tr>\n      <th>29</th>\n      <td>2001-06</td>\n      <td>0.608905</td>\n    </tr>\n    <tr>\n      <th>30</th>\n      <td>2001-07</td>\n      <td>0.608568</td>\n    </tr>\n    <tr>\n      <th>31</th>\n      <td>2001-08</td>\n      <td>0.626717</td>\n    </tr>\n    <tr>\n      <th>32</th>\n      <td>2001-09</td>\n      <td>0.622910</td>\n    </tr>\n    <tr>\n      <th>33</th>\n      <td>2001-10</td>\n      <td>0.623935</td>\n    </tr>\n    <tr>\n      <th>34</th>\n      <td>2001-11</td>\n      <td>0.618375</td>\n    </tr>\n    <tr>\n      <th>35</th>\n      <td>2001-12</td>\n      <td>0.620119</td>\n    </tr>\n    <tr>\n      <th>36</th>\n      <td>2002-01</td>\n      <td>0.616593</td>\n    </tr>\n    <tr>\n      <th>37</th>\n      <td>2002-02</td>\n      <td>0.611603</td>\n    </tr>\n    <tr>\n      <th>38</th>\n      <td>2002-03</td>\n      <td>0.615735</td>\n    </tr>\n    <tr>\n      <th>39</th>\n      <td>2002-04</td>\n      <td>0.614071</td>\n    </tr>\n    <tr>\n      <th>40</th>\n      <td>2002-05</td>\n      <td>0.628227</td>\n    </tr>\n    <tr>\n      <th>41</th>\n      <td>2002-06</td>\n      <td>0.644050</td>\n    </tr>\n    <tr>\n      <th>42</th>\n      <td>2002-07</td>\n      <td>0.638700</td>\n    </tr>\n    <tr>\n      <th>43</th>\n      <td>2002-08</td>\n      <td>0.636332</td>\n    </tr>\n    <tr>\n      <th>44</th>\n      <td>2002-09</td>\n      <td>0.630588</td>\n    </tr>\n    <tr>\n      <th>45</th>\n      <td>2002-10</td>\n      <td>0.629941</td>\n    </tr>\n    <tr>\n      <th>46</th>\n      <td>2002-11</td>\n      <td>0.637086</td>\n    </tr>\n    <tr>\n      <th>47</th>\n      <td>2002-12</td>\n      <td>0.642175</td>\n    </tr>\n    <tr>\n      <th>48</th>\n      <td>2003-01</td>\n      <td>0.657109</td>\n    </tr>\n    <tr>\n      <th>49</th>\n      <td>2003-02</td>\n      <td>0.669772</td>\n    </tr>\n    <tr>\n      <th>50</th>\n      <td>2003-03</td>\n      <td>0.682548</td>\n    </tr>\n    <tr>\n      <th>51</th>\n      <td>2003-04</td>\n      <td>0.689020</td>\n    </tr>\n    <tr>\n      <th>52</th>\n      <td>2003-05</td>\n      <td>0.713219</td>\n    </tr>\n    <tr>\n      <th>53</th>\n      <td>2003-06</td>\n      <td>0.702240</td>\n    </tr>\n    <tr>\n      <th>54</th>\n      <td>2003-07</td>\n      <td>0.700448</td>\n    </tr>\n    <tr>\n      <th>55</th>\n      <td>2003-08</td>\n      <td>0.699193</td>\n    </tr>\n    <tr>\n      <th>56</th>\n      <td>2003-09</td>\n      <td>0.696927</td>\n    </tr>\n    <tr>\n      <th>57</th>\n      <td>2003-10</td>\n      <td>0.697630</td>\n    </tr>\n    <tr>\n      <th>58</th>\n      <td>2003-11</td>\n      <td>0.692778</td>\n    </tr>\n    <tr>\n      <th>59</th>\n      <td>2003-12</td>\n      <td>0.701957</td>\n    </tr>\n    <tr>\n      <th>60</th>\n      <td>2004-01</td>\n      <td>0.692145</td>\n    </tr>\n    <tr>\n      <th>61</th>\n      <td>2004-02</td>\n      <td>0.676898</td>\n    </tr>\n    <tr>\n      <th>62</th>\n      <td>2004-03</td>\n      <td>0.671241</td>\n    </tr>\n    <tr>\n      <th>63</th>\n      <td>2004-04</td>\n      <td>0.665325</td>\n    </tr>\n    <tr>\n      <th>64</th>\n      <td>2004-05</td>\n      <td>0.671574</td>\n    </tr>\n    <tr>\n      <th>65</th>\n      <td>2004-06</td>\n      <td>0.664282</td>\n    </tr>\n    <tr>\n      <th>66</th>\n      <td>2004-07</td>\n      <td>0.665757</td>\n    </tr>\n    <tr>\n      <th>67</th>\n      <td>2004-08</td>\n      <td>0.669418</td>\n    </tr>\n    <tr>\n      <th>68</th>\n      <td>2004-09</td>\n      <td>0.681298</td>\n    </tr>\n    <tr>\n      <th>69</th>\n      <td>2004-10</td>\n      <td>0.691440</td>\n    </tr>\n    <tr>\n      <th>70</th>\n      <td>2004-11</td>\n      <td>0.698620</td>\n    </tr>\n    <tr>\n      <th>71</th>\n      <td>2004-12</td>\n      <td>0.695000</td>\n    </tr>\n    <tr>\n      <th>72</th>\n      <td>2005-01</td>\n      <td>0.698667</td>\n    </tr>\n    <tr>\n      <th>73</th>\n      <td>2005-02</td>\n      <td>0.689680</td>\n    </tr>\n    <tr>\n      <th>74</th>\n      <td>2005-03</td>\n      <td>0.692331</td>\n    </tr>\n    <tr>\n      <th>75</th>\n      <td>2005-04</td>\n      <td>0.682933</td>\n    </tr>\n    <tr>\n      <th>76</th>\n      <td>2005-05</td>\n      <td>0.683993</td>\n    </tr>\n    <tr>\n      <th>77</th>\n      <td>2005-06</td>\n      <td>0.668948</td>\n    </tr>\n    <tr>\n      <th>78</th>\n      <td>2005-07</td>\n      <td>0.687564</td>\n    </tr>\n    <tr>\n      <th>79</th>\n      <td>2005-08</td>\n      <td>0.685270</td>\n    </tr>\n    <tr>\n      <th>80</th>\n      <td>2005-09</td>\n      <td>0.677595</td>\n    </tr>\n    <tr>\n      <th>81</th>\n      <td>2005-10</td>\n      <td>0.681367</td>\n    </tr>\n    <tr>\n      <th>82</th>\n      <td>2005-11</td>\n      <td>0.679332</td>\n    </tr>\n    <tr>\n      <th>83</th>\n      <td>2005-12</td>\n      <td>0.679221</td>\n    </tr>\n    <tr>\n      <th>84</th>\n      <td>2006-01</td>\n      <td>0.685984</td>\n    </tr>\n    <tr>\n      <th>85</th>\n      <td>2006-02</td>\n      <td>0.682972</td>\n    </tr>\n    <tr>\n      <th>86</th>\n      <td>2006-03</td>\n      <td>0.689348</td>\n    </tr>\n    <tr>\n      <th>87</th>\n      <td>2006-04</td>\n      <td>0.694628</td>\n    </tr>\n    <tr>\n      <th>88</th>\n      <td>2006-05</td>\n      <td>0.683295</td>\n    </tr>\n    <tr>\n      <th>89</th>\n      <td>2006-06</td>\n      <td>0.686659</td>\n    </tr>\n    <tr>\n      <th>90</th>\n      <td>2006-07</td>\n      <td>0.687819</td>\n    </tr>\n    <tr>\n      <th>91</th>\n      <td>2006-08</td>\n      <td>0.676687</td>\n    </tr>\n    <tr>\n      <th>92</th>\n      <td>2006-09</td>\n      <td>0.675107</td>\n    </tr>\n    <tr>\n      <th>93</th>\n      <td>2006-10</td>\n      <td>0.672543</td>\n    </tr>\n    <tr>\n      <th>94</th>\n      <td>2006-11</td>\n      <td>0.673968</td>\n    </tr>\n    <tr>\n      <th>95</th>\n      <td>2006-12</td>\n      <td>0.672861</td>\n    </tr>\n    <tr>\n      <th>96</th>\n      <td>2007-01</td>\n      <td>0.663407</td>\n    </tr>\n    <tr>\n      <th>97</th>\n      <td>2007-02</td>\n      <td>0.668003</td>\n    </tr>\n    <tr>\n      <th>98</th>\n      <td>2007-03</td>\n      <td>0.680211</td>\n    </tr>\n    <tr>\n      <th>99</th>\n      <td>2007-04</td>\n      <td>0.679337</td>\n    </tr>\n    <tr>\n      <th>100</th>\n      <td>2007-05</td>\n      <td>0.681356</td>\n    </tr>\n    <tr>\n      <th>101</th>\n      <td>2007-06</td>\n      <td>0.675624</td>\n    </tr>\n    <tr>\n      <th>102</th>\n      <td>2007-07</td>\n      <td>0.674400</td>\n    </tr>\n    <tr>\n      <th>103</th>\n      <td>2007-08</td>\n      <td>0.677663</td>\n    </tr>\n    <tr>\n      <th>104</th>\n      <td>2007-09</td>\n      <td>0.688870</td>\n    </tr>\n    <tr>\n      <th>105</th>\n      <td>2007-10</td>\n      <td>0.696141</td>\n    </tr>\n    <tr>\n      <th>106</th>\n      <td>2007-11</td>\n      <td>0.708959</td>\n    </tr>\n    <tr>\n      <th>107</th>\n      <td>2007-12</td>\n      <td>0.720637</td>\n    </tr>\n    <tr>\n      <th>108</th>\n      <td>2008-01</td>\n      <td>0.747250</td>\n    </tr>\n    <tr>\n      <th>109</th>\n      <td>2008-02</td>\n      <td>0.750938</td>\n    </tr>\n    <tr>\n      <th>110</th>\n      <td>2008-03</td>\n      <td>0.774939</td>\n    </tr>\n    <tr>\n      <th>111</th>\n      <td>2008-04</td>\n      <td>0.794866</td>\n    </tr>\n    <tr>\n      <th>112</th>\n      <td>2008-05</td>\n      <td>0.792086</td>\n    </tr>\n    <tr>\n      <th>113</th>\n      <td>2008-06</td>\n      <td>0.791524</td>\n    </tr>\n    <tr>\n      <th>114</th>\n      <td>2008-07</td>\n      <td>0.793076</td>\n    </tr>\n    <tr>\n      <th>115</th>\n      <td>2008-08</td>\n      <td>0.792788</td>\n    </tr>\n    <tr>\n      <th>116</th>\n      <td>2008-09</td>\n      <td>0.799243</td>\n    </tr>\n    <tr>\n      <th>117</th>\n      <td>2008-10</td>\n      <td>0.786680</td>\n    </tr>\n    <tr>\n      <th>118</th>\n      <td>2008-11</td>\n      <td>0.830632</td>\n    </tr>\n    <tr>\n      <th>119</th>\n      <td>2008-12</td>\n      <td>0.904476</td>\n    </tr>\n    <tr>\n      <th>120</th>\n      <td>2009-01</td>\n      <td>0.918193</td>\n    </tr>\n    <tr>\n      <th>121</th>\n      <td>2009-02</td>\n      <td>0.886910</td>\n    </tr>\n    <tr>\n      <th>122</th>\n      <td>2009-03</td>\n      <td>0.919664</td>\n    </tr>\n    <tr>\n      <th>123</th>\n      <td>2009-04</td>\n      <td>0.897560</td>\n    </tr>\n    <tr>\n      <th>124</th>\n      <td>2009-05</td>\n      <td>0.884445</td>\n    </tr>\n    <tr>\n      <th>125</th>\n      <td>2009-06</td>\n      <td>0.856700</td>\n    </tr>\n    <tr>\n      <th>126</th>\n      <td>2009-07</td>\n      <td>0.860920</td>\n    </tr>\n    <tr>\n      <th>127</th>\n      <td>2009-08</td>\n      <td>0.862655</td>\n    </tr>\n    <tr>\n      <th>128</th>\n      <td>2009-09</td>\n      <td>0.891348</td>\n    </tr>\n    <tr>\n      <th>129</th>\n      <td>2009-10</td>\n      <td>0.915566</td>\n    </tr>\n    <tr>\n      <th>130</th>\n      <td>2009-11</td>\n      <td>0.898924</td>\n    </tr>\n    <tr>\n      <th>131</th>\n      <td>2009-12</td>\n      <td>0.899717</td>\n    </tr>\n    <tr>\n      <th>132</th>\n      <td>2010-01</td>\n      <td>0.883050</td>\n    </tr>\n    <tr>\n      <th>133</th>\n      <td>2010-02</td>\n      <td>0.876042</td>\n    </tr>\n    <tr>\n      <th>134</th>\n      <td>2010-03</td>\n      <td>0.901602</td>\n    </tr>\n    <tr>\n      <th>135</th>\n      <td>2010-04</td>\n      <td>0.874555</td>\n    </tr>\n    <tr>\n      <th>136</th>\n      <td>2010-05</td>\n      <td>0.857144</td>\n    </tr>\n    <tr>\n      <th>137</th>\n      <td>2010-06</td>\n      <td>0.827707</td>\n    </tr>\n    <tr>\n      <th>138</th>\n      <td>2010-07</td>\n      <td>0.835657</td>\n    </tr>\n    <tr>\n      <th>139</th>\n      <td>2010-08</td>\n      <td>0.823632</td>\n    </tr>\n    <tr>\n      <th>140</th>\n      <td>2010-09</td>\n      <td>0.839866</td>\n    </tr>\n    <tr>\n      <th>141</th>\n      <td>2010-10</td>\n      <td>0.876376</td>\n    </tr>\n    <tr>\n      <th>142</th>\n      <td>2010-11</td>\n      <td>0.855095</td>\n    </tr>\n    <tr>\n      <th>143</th>\n      <td>2010-12</td>\n      <td>0.848128</td>\n    </tr>\n    <tr>\n      <th>144</th>\n      <td>2011-01</td>\n      <td>0.847117</td>\n    </tr>\n    <tr>\n      <th>145</th>\n      <td>2011-02</td>\n      <td>0.846355</td>\n    </tr>\n    <tr>\n      <th>146</th>\n      <td>2011-03</td>\n      <td>0.866533</td>\n    </tr>\n    <tr>\n      <th>147</th>\n      <td>2011-04</td>\n      <td>0.882913</td>\n    </tr>\n    <tr>\n      <th>148</th>\n      <td>2011-05</td>\n      <td>0.877877</td>\n    </tr>\n    <tr>\n      <th>149</th>\n      <td>2011-06</td>\n      <td>0.887448</td>\n    </tr>\n    <tr>\n      <th>150</th>\n      <td>2011-07</td>\n      <td>0.884760</td>\n    </tr>\n    <tr>\n      <th>151</th>\n      <td>2011-08</td>\n      <td>0.876685</td>\n    </tr>\n    <tr>\n      <th>152</th>\n      <td>2011-09</td>\n      <td>0.871723</td>\n    </tr>\n    <tr>\n      <th>153</th>\n      <td>2011-10</td>\n      <td>0.870360</td>\n    </tr>\n    <tr>\n      <th>154</th>\n      <td>2011-11</td>\n      <td>0.857395</td>\n    </tr>\n    <tr>\n      <th>155</th>\n      <td>2011-12</td>\n      <td>0.844055</td>\n    </tr>\n    <tr>\n      <th>156</th>\n      <td>2012-01</td>\n      <td>0.832102</td>\n    </tr>\n    <tr>\n      <th>157</th>\n      <td>2012-02</td>\n      <td>0.836960</td>\n    </tr>\n    <tr>\n      <th>158</th>\n      <td>2012-03</td>\n      <td>0.834482</td>\n    </tr>\n    <tr>\n      <th>159</th>\n      <td>2012-04</td>\n      <td>0.821884</td>\n    </tr>\n    <tr>\n      <th>160</th>\n      <td>2012-05</td>\n      <td>0.803708</td>\n    </tr>\n    <tr>\n      <th>161</th>\n      <td>2012-06</td>\n      <td>0.805793</td>\n    </tr>\n    <tr>\n      <th>162</th>\n      <td>2012-07</td>\n      <td>0.788266</td>\n    </tr>\n    <tr>\n      <th>163</th>\n      <td>2012-08</td>\n      <td>0.788837</td>\n    </tr>\n    <tr>\n      <th>164</th>\n      <td>2012-09</td>\n      <td>0.798211</td>\n    </tr>\n    <tr>\n      <th>165</th>\n      <td>2012-10</td>\n      <td>0.806652</td>\n    </tr>\n    <tr>\n      <th>166</th>\n      <td>2012-11</td>\n      <td>0.803889</td>\n    </tr>\n    <tr>\n      <th>167</th>\n      <td>2012-12</td>\n      <td>0.812368</td>\n    </tr>\n    <tr>\n      <th>168</th>\n      <td>2013-01</td>\n      <td>0.832709</td>\n    </tr>\n    <tr>\n      <th>169</th>\n      <td>2013-02</td>\n      <td>0.862498</td>\n    </tr>\n    <tr>\n      <th>170</th>\n      <td>2013-03</td>\n      <td>0.859955</td>\n    </tr>\n    <tr>\n      <th>171</th>\n      <td>2013-04</td>\n      <td>0.850757</td>\n    </tr>\n    <tr>\n      <th>172</th>\n      <td>2013-05</td>\n      <td>0.849143</td>\n    </tr>\n    <tr>\n      <th>173</th>\n      <td>2013-06</td>\n      <td>0.851910</td>\n    </tr>\n    <tr>\n      <th>174</th>\n      <td>2013-07</td>\n      <td>0.861924</td>\n    </tr>\n    <tr>\n      <th>175</th>\n      <td>2013-08</td>\n      <td>0.859041</td>\n    </tr>\n    <tr>\n      <th>176</th>\n      <td>2013-09</td>\n      <td>0.841710</td>\n    </tr>\n    <tr>\n      <th>177</th>\n      <td>2013-10</td>\n      <td>0.847198</td>\n    </tr>\n    <tr>\n      <th>178</th>\n      <td>2013-11</td>\n      <td>0.837802</td>\n    </tr>\n    <tr>\n      <th>179</th>\n      <td>2013-12</td>\n      <td>0.836387</td>\n    </tr>\n    <tr>\n      <th>180</th>\n      <td>2014-01</td>\n      <td>0.826743</td>\n    </tr>\n    <tr>\n      <th>181</th>\n      <td>2014-02</td>\n      <td>0.825099</td>\n    </tr>\n    <tr>\n      <th>182</th>\n      <td>2014-03</td>\n      <td>0.831698</td>\n    </tr>\n    <tr>\n      <th>183</th>\n      <td>2014-04</td>\n      <td>0.825195</td>\n    </tr>\n    <tr>\n      <th>184</th>\n      <td>2014-05</td>\n      <td>0.815347</td>\n    </tr>\n    <tr>\n      <th>185</th>\n      <td>2014-06</td>\n      <td>0.804090</td>\n    </tr>\n    <tr>\n      <th>186</th>\n      <td>2014-07</td>\n      <td>0.793104</td>\n    </tr>\n    <tr>\n      <th>187</th>\n      <td>2014-08</td>\n      <td>0.797301</td>\n    </tr>\n    <tr>\n      <th>188</th>\n      <td>2014-09</td>\n      <td>0.791132</td>\n    </tr>\n    <tr>\n      <th>189</th>\n      <td>2014-10</td>\n      <td>0.788609</td>\n    </tr>\n    <tr>\n      <th>190</th>\n      <td>2014-11</td>\n      <td>0.790535</td>\n    </tr>\n    <tr>\n      <th>191</th>\n      <td>2014-12</td>\n      <td>0.788300</td>\n    </tr>\n    <tr>\n      <th>192</th>\n      <td>2015-01</td>\n      <td>0.766798</td>\n    </tr>\n    <tr>\n      <th>193</th>\n      <td>2015-02</td>\n      <td>0.740507</td>\n    </tr>\n    <tr>\n      <th>194</th>\n      <td>2015-03</td>\n      <td>0.723584</td>\n    </tr>\n    <tr>\n      <th>195</th>\n      <td>2015-04</td>\n      <td>0.721158</td>\n    </tr>\n    <tr>\n      <th>196</th>\n      <td>2015-05</td>\n      <td>0.721241</td>\n    </tr>\n    <tr>\n      <th>197</th>\n      <td>2015-06</td>\n      <td>0.720780</td>\n    </tr>\n    <tr>\n      <th>198</th>\n      <td>2015-07</td>\n      <td>0.706850</td>\n    </tr>\n    <tr>\n      <th>199</th>\n      <td>2015-08</td>\n      <td>0.714232</td>\n    </tr>\n    <tr>\n      <th>200</th>\n      <td>2015-09</td>\n      <td>0.731289</td>\n    </tr>\n    <tr>\n      <th>201</th>\n      <td>2015-10</td>\n      <td>0.732870</td>\n    </tr>\n    <tr>\n      <th>202</th>\n      <td>2015-11</td>\n      <td>0.706576</td>\n    </tr>\n    <tr>\n      <th>203</th>\n      <td>2015-12</td>\n      <td>0.725952</td>\n    </tr>\n    <tr>\n      <th>204</th>\n      <td>2016-01</td>\n      <td>0.754586</td>\n    </tr>\n    <tr>\n      <th>205</th>\n      <td>2016-02</td>\n      <td>0.775585</td>\n    </tr>\n    <tr>\n      <th>206</th>\n      <td>2016-03</td>\n      <td>0.780201</td>\n    </tr>\n    <tr>\n      <th>207</th>\n      <td>2016-04</td>\n      <td>0.792296</td>\n    </tr>\n    <tr>\n      <th>208</th>\n      <td>2016-05</td>\n      <td>0.777791</td>\n    </tr>\n    <tr>\n      <th>209</th>\n      <td>2016-06</td>\n      <td>0.790494</td>\n    </tr>\n    <tr>\n      <th>210</th>\n      <td>2016-07</td>\n      <td>0.841058</td>\n    </tr>\n    <tr>\n      <th>211</th>\n      <td>2016-08</td>\n      <td>0.855209</td>\n    </tr>\n    <tr>\n      <th>212</th>\n      <td>2016-09</td>\n      <td>0.852277</td>\n    </tr>\n    <tr>\n      <th>213</th>\n      <td>2016-10</td>\n      <td>0.893900</td>\n    </tr>\n    <tr>\n      <th>214</th>\n      <td>2016-11</td>\n      <td>0.868943</td>\n    </tr>\n    <tr>\n      <th>215</th>\n      <td>2016-12</td>\n      <td>0.844414</td>\n    </tr>\n    <tr>\n      <th>216</th>\n      <td>2017-01</td>\n      <td>0.861004</td>\n    </tr>\n    <tr>\n      <th>217</th>\n      <td>2017-02</td>\n      <td>0.852730</td>\n    </tr>\n    <tr>\n      <th>218</th>\n      <td>2017-03</td>\n      <td>0.865603</td>\n    </tr>\n    <tr>\n      <th>219</th>\n      <td>2017-04</td>\n      <td>0.848235</td>\n    </tr>\n    <tr>\n      <th>220</th>\n      <td>2017-05</td>\n      <td>0.855543</td>\n    </tr>\n    <tr>\n      <th>221</th>\n      <td>2017-06</td>\n      <td>0.877238</td>\n    </tr>\n    <tr>\n      <th>222</th>\n      <td>2017-07</td>\n      <td>0.886173</td>\n    </tr>\n    <tr>\n      <th>223</th>\n      <td>2017-08</td>\n      <td>0.911207</td>\n    </tr>\n    <tr>\n      <th>224</th>\n      <td>2017-09</td>\n      <td>0.894701</td>\n    </tr>\n    <tr>\n      <th>225</th>\n      <td>2017-10</td>\n      <td>0.890714</td>\n    </tr>\n    <tr>\n      <th>226</th>\n      <td>2017-11</td>\n      <td>0.887945</td>\n    </tr>\n    <tr>\n      <th>227</th>\n      <td>2017-12</td>\n      <td>0.882649</td>\n    </tr>\n    <tr>\n      <th>228</th>\n      <td>2018-01</td>\n      <td>0.883311</td>\n    </tr>\n    <tr>\n      <th>229</th>\n      <td>2018-02</td>\n      <td>0.883964</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>2018-03</td>\n      <td>0.882870</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>2018-04</td>\n      <td>0.872121</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>2018-05</td>\n      <td>0.877258</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>2018-06</td>\n      <td>0.878860</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>2018-07</td>\n      <td>0.887255</td>\n    </tr>\n    <tr>\n      <th>235</th>\n      <td>2018-08</td>\n      <td>0.896869</td>\n    </tr>\n    <tr>\n      <th>236</th>\n      <td>2018-09</td>\n      <td>0.892807</td>\n    </tr>\n    <tr>\n      <th>237</th>\n      <td>2018-10</td>\n      <td>0.882721</td>\n    </tr>\n    <tr>\n      <th>238</th>\n      <td>2018-11</td>\n      <td>0.881181</td>\n    </tr>\n    <tr>\n      <th>239</th>\n      <td>2018-12</td>\n      <td>0.897742</td>\n    </tr>\n    <tr>\n      <th>240</th>\n      <td>2019-01</td>\n      <td>0.886030</td>\n    </tr>\n    <tr>\n      <th>241</th>\n      <td>2019-02</td>\n      <td>0.872637</td>\n    </tr>\n    <tr>\n      <th>242</th>\n      <td>2019-03</td>\n      <td>0.858220</td>\n    </tr>\n    <tr>\n      <th>243</th>\n      <td>2019-04</td>\n      <td>0.861789</td>\n    </tr>\n    <tr>\n      <th>244</th>\n      <td>2019-05</td>\n      <td>0.871758</td>\n    </tr>\n    <tr>\n      <th>245</th>\n      <td>2019-06</td>\n      <td>0.891073</td>\n    </tr>\n    <tr>\n      <th>246</th>\n      <td>2019-07</td>\n      <td>0.899420</td>\n    </tr>\n    <tr>\n      <th>247</th>\n      <td>2019-08</td>\n      <td>0.915538</td>\n    </tr>\n    <tr>\n      <th>248</th>\n      <td>2019-09</td>\n      <td>0.890916</td>\n    </tr>\n    <tr>\n      <th>249</th>\n      <td>2019-10</td>\n      <td>0.875386</td>\n    </tr>\n    <tr>\n      <th>250</th>\n      <td>2019-11</td>\n      <td>0.857609</td>\n    </tr>\n    <tr>\n      <th>251</th>\n      <td>2019-12</td>\n      <td>0.847307</td>\n    </tr>\n    <tr>\n      <th>252</th>\n      <td>2020-01</td>\n      <td>0.849273</td>\n    </tr>\n    <tr>\n      <th>253</th>\n      <td>2020-02</td>\n      <td>0.840946</td>\n    </tr>\n    <tr>\n      <th>254</th>\n      <td>2020-03</td>\n      <td>0.894595</td>\n    </tr>\n    <tr>\n      <th>255</th>\n      <td>2020-04</td>\n      <td>0.875469</td>\n    </tr>\n    <tr>\n      <th>256</th>\n      <td>2020-05</td>\n      <td>0.886853</td>\n    </tr>\n    <tr>\n      <th>257</th>\n      <td>2020-06</td>\n      <td>0.898781</td>\n    </tr>\n    <tr>\n      <th>258</th>\n      <td>2020-07</td>\n      <td>0.904667</td>\n    </tr>\n    <tr>\n      <th>259</th>\n      <td>2020-08</td>\n      <td>0.900809</td>\n    </tr>\n    <tr>\n      <th>260</th>\n      <td>2020-09</td>\n      <td>0.909474</td>\n    </tr>\n    <tr>\n      <th>261</th>\n      <td>2020-10</td>\n      <td>0.907411</td>\n    </tr>\n    <tr>\n      <th>262</th>\n      <td>2020-11</td>\n      <td>0.896053</td>\n    </tr>\n    <tr>\n      <th>263</th>\n      <td>2020-12</td>\n      <td>0.906244</td>\n    </tr>\n    <tr>\n      <th>264</th>\n      <td>2021-01</td>\n      <td>0.892665</td>\n    </tr>\n    <tr>\n      <th>265</th>\n      <td>2021-02</td>\n      <td>0.872683</td>\n    </tr>\n    <tr>\n      <th>266</th>\n      <td>2021-03</td>\n      <td>0.858732</td>\n    </tr>\n    <tr>\n      <th>267</th>\n      <td>2021-04</td>\n      <td>0.865268</td>\n    </tr>\n    <tr>\n      <th>268</th>\n      <td>2021-05</td>\n      <td>0.862583</td>\n    </tr>\n    <tr>\n      <th>269</th>\n      <td>2021-06</td>\n      <td>0.858720</td>\n    </tr>\n    <tr>\n      <th>270</th>\n      <td>2021-07</td>\n      <td>0.856130</td>\n    </tr>\n    <tr>\n      <th>271</th>\n      <td>2021-08</td>\n      <td>0.852874</td>\n    </tr>\n    <tr>\n      <th>272</th>\n      <td>2021-09</td>\n      <td>0.856833</td>\n    </tr>\n    <tr>\n      <th>273</th>\n      <td>2021-10</td>\n      <td>0.846944</td>\n    </tr>\n    <tr>\n      <th>274</th>\n      <td>2021-11</td>\n      <td>0.847864</td>\n    </tr>\n    <tr>\n      <th>275</th>\n      <td>2021-12</td>\n      <td>0.848748</td>\n    </tr>\n    <tr>\n      <th>276</th>\n      <td>2022-01</td>\n      <td>0.835034</td>\n    </tr>\n    <tr>\n      <th>277</th>\n      <td>2022-02</td>\n      <td>0.837873</td>\n    </tr>\n  </tbody>\n</table>",
    "message": "Successful operation",
    "return_code": 0
}

Note: in case of error, application will return errorcode along with error line no as data.
