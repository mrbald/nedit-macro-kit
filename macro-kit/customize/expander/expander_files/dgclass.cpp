// construcor without ancestor
\1::\1(
	ty_pt_nodeBase pt_father,
	ty_localID li,
	ty_repere ri):
		ty_drawableNodeBase(
			pt_father,
			li,
			createDefaultNodeContainer(),
			ri,
			ty_sphericalBB(0))
{
	
}

// with ancestor
\1::\1(
	ty_pt_nodeBase pt_father,
	ty_localID li,
	ty_repere ri,
	ty_nodeBase& _ancestor):
		ty_drawableNodeBase(
			pt_father,
			li,
			createDefaultNodeContainer(),
			_ancestor,
			ri,
			ty_sphericalBB(_ty_2d(_ancestor).boundingBox.radius))
{
	
}

// death function
void \1::deathDay()
{
	
}

/// generation
void \1::upDown(parserFunction::ty_generation& v)
{
	setMaturity(v.getNodeInfo());
	
	if(precision()>0)
	{
		// new generation
		childGeneration(v);
	}
	else
	{
		// this is a drawable node
		draw();
	}
}

/// \1 output.
std::ostream& \1::output(std::ostream& os) const
{
	
}

/// next generation generation
void \1::childGeneration(parserFunction::ty_generation& v)
{
	
}

/// opengl draw function
void \1::drawCore()
{
	
}

/// opengl debug draw function
void \1::drawDebug(ty_glViewer&)
{
	
}

/// set maturity
void \1::setMaturity(ty_visualProperty& vp)
{
	static ty_float ln2 = math::ln(2);
	
	ty_float estimatedArea = boundingBox.radius/vp.getDistanceFromCenter();
	ty_float p = math::ln(dpGV::sliderF(6,1)*20*estimatedArea)/ln2;
	ty_maturity::setPrecision(p);
	
	ty_float speed = dpGV::sliderF(6,4)*0.5;
	
	ty_float x1 = -dpGV::sliderF(6,2);
	ty_float x2 = -dpGV::sliderF(6,3);
	
	if(isAncestorValid() && (math::abs(ancestor().ty_maturity::precision()-p)<dpGV::sliderF(6,5)))
	{
		ty_float m=ancestor().ty_maturity::maturity();
		if(p<x1)
		{
			m-=speed;
		}
		if(p>x2)
		{
			m+=speed;
		}

		m=(m>0)?m:0;
		m=(m<1)?m:1;
		ty_maturity::setMaturity(m);
	}
	else
	{
		ty_maturity::setMaturity((p<((x1+x2)*0.5))?0:1);
	}
}
